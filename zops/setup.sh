#!/bin/bash
# zops一键部署脚本

# get current dir
cur_dir=$(cd `dirname $0`; pwd)

MASTER_IP=$1

if [ -z "$MASTER_IP" ]
then
    echo -e "Usge: $0 master_ip"
    echo -e "$0 127.0.0.1"
    exit 1
fi

function install_lib(){
    cd $cur_dir
    rm -fr dist/src/*
    cd dist/src/
    result=0
    err_msg=""
    # install setuptools
    if ! python -c 'import setuptools' >/dev/null 2>&1
    then
        tar xf ../dist/setuptools-0.6c11.tar.gz
        cd setuptools-0.6c11/
        python setup.py build
        python setup.py install
        if [ $? -ne 0 ];then
            echo 'install setuptools fail'
            return 1
        fi
        cd ..
    fi
    # install gevent
    if ! python -c 'import gevent' >/dev/null 2>&1
    then
        yum -y install python-devel
        tar xf ../dist/libev-4.15.tar.gz
        cd libev-4.15/
        ./configure
        make && make install
        cd ..
        unzip -x ../dist/greenlet-0.4.2.zip
        cd greenlet-0.4.2/
        python setup.py build
        python setup.py install
        cd ..
        tar xf ../dist/gevent-1.0.1.tar.gz
        cd gevent-1.0.1/
        python setup.py build
        python setup.py install
        if [ $? -ne 0 ];then
            result=1
            err_msg=$err_msg"|gevent安装失败"
        fi
        cd ..
    fi
    # install zeromq
    if ! python -c 'import zmq' >/dev/null 2>&1
    then
        tar xf ../dist/zeromq-4.0.4.tar.gz
        cd zeromq-4.0.4/
        ./configure
        make && make install
        cd ..
        tar xf ../dist/pyzmq-14.3.1.tar.gz
        cd pyzmq-14.3.1/
        python setup.py build
        python setup.py install
        if [ $? -ne 0 ];then
            result=1
            err_msg=$err_msg"|zeromq安装失败"
        fi
        cd ..
    fi
    # install APScheduler
    if ! python -c 'import apscheduler' >/dev/null 2>&1
    then
		tar xf ../dist/futures-2.1.6.tar.gz
		cd futures-2.1.6/
		python setup.py build
        python setup.py install
		cd ..
		easy_install ../dist/pytz-2014.4-py2.6.egg
		unzip -x ../dist/tzlocal-1.1.1.zip
		cd tzlocal-1.1.1/
		python setup.py build
        python setup.py install
		cd ..
		tar xf ../dist/six-1.7.3.tar.gz 
		cd six-1.7.3/
		python setup.py build
        python setup.py install
		cd ..
        tar xf ../dist/APScheduler-3.0.0rc1.tar.gz
        cd APScheduler-3.0.0rc1/
        python setup.py build
        python setup.py install
        if [ $? -ne 0 ];then
            result=1
            err_msg=$err_msg"|APScheduler安装失败"
        fi
        cd ..
    fi
    # install mlogging
    if ! python -c 'import mlogging' >/dev/null 2>&1
    then
        tar xf ../dist/mlogging.tar.gz
        cd mlogging/
        python setup.py build
        python setup.py install
        if [ $? -ne 0 ];then
            result=1
            err_msg=$err_msg"|mlogging安装失败"
        fi
        cd ..
    fi
    # install msgpack
    if ! python -c 'import msgpack' >/dev/null 2>&1
    then
        tar xf ../dist/msgpack-python-0.4.2.tar.gz
        cd msgpack-python-0.4.2/
        python setup.py build
        python setup.py install
        if [ $? -ne 0 ];then
            result=1
            err_msg=$err_msg"|msgpack安装失败"
        fi
        cd ..
    fi
    #
    if [ $result -ne 0 ];then
        echo $err_msg
        return 2
    fi
    return 0
}

function install_zops(){
    cd $cur_dir
    lan_ip=$(/sbin/ifconfig|grep 'inet addr'|awk -F\: '{print $2}'|awk '{if($1~/192.168.|172.16./){print $1}}'|head -1)
    sed -i "s/local_ip = .*/local_ip = ${lan_ip}/" zops/agent/conf/client.conf
    sed -i "s/master = .*/master = ${MASTER_IP}/" zops/agent/conf/client.conf
    mkdir -p /data/ops
    if [ -d /data/ops/zops ];then
        rm -fr /data/ops/zops
    fi
    /bin/cp -a zops /data/ops/
    if [ $? -ne 0 ];then
        echo "zops拷贝失败"
        return 1
    fi
    cd ~
    sed -i '/bin\/zops_keep_watch.sh/d' /var/spool/cron/root
    echo '*  *  *  *  * /bin/bash /data/ops/zops/agent/bin/zops_keep_watch.sh >> /var/log/zops_keep_watch 2>&1' >> /var/spool/cron/root
    return 0
}

function main(){
    echo "开始部署环境、安装zops，详细日志请查看/tmp/zops_install.log"
    install_lib > /tmp/zops_install.log 2>&1
    if [ $? -ne 0 ];then
        echo -e "zops环境部署[\033[0;31;1m失败\033[0m]，请检查日志"
        return 1
    fi
    install_zops >> /tmp/zops_install.log 2>&1
    if [ $? -ne 0 ];then
        echo -e "zops代码部署[\033[0;31;1m失败\033[0m]，请检查日志"
        return 2
    fi
    /bin/bash /data/ops/zops/agent/bin/zops_agent.sh restart
    echo "zops部署、安装完毕"
}

main