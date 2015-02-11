#!/bin/bash

#java环境发布脚本
#注释：$1 = 容器类型，$2 = 项目名称，$3 = 文件名称

DATE=`date +%Y-%m-%d`
Time=`date +"%Y-%m-%d%H:%M"`
Log="/tmp/deploy_error.log"
Backup="/data/war-backup"
Jboss_path="/data/jboss/server/default/deploy"
Jetty_path="/data/jetty/webapps"
STATU="/mnt/app_shell/meizuyw/release/do_iptables.sh"
App_name=$2
War1=$3
Domain=$4
Ipaddr=`/sbin/ifconfig |grep -A2 "eth0" |awk -F':' '{if($2 ~ /^[0-9][0-9][0-9]\./)print $2}' |cut -d" " -f 1`



   if [ ! -d $Backup/$DATE ];then

      mkdir -p $Backup/$DATE

   fi


  HELP(){

             echo "USAG: 详细信息如下
             $PATH_SH/fublish.sh jboss/jetty  warname  warfile Domain
             1、 业务对应的容器类型
             2、 对应的业务war包名
             3、 文件路径"


          }   



#  JBOSS(){
#       
#          $STATU down > /dev/null
#
#           
#           if [ ! X${War1} = X ];then      
#
#             /usr/bin/killall -9 java > /dev/null
#
#             #type1=`basename $War1|awk -F '.' '{print $4}'`
#             type1=`echo $War1|awk -F "." '{print $NF}'`
#
#             if [ $type1 = "war" ];then
#
#                   Bak=`ls ${Backup}/${DATE}|wc -l`
#                   if [ $Bak -eq 0 ];then
#                        old_war=`ls -ld $Jboss_path/$App_name.war` 
#                        #cd $Jboss_path && cp -r "$old_war" $Backup/$DATE && rm -rf  "$Jboss_path/$App_name-*.war"
#                        cd $Jboss_path && mv "$old_war" $Backup/$DATE 
#                        cp $War1 $Jboss_path && chown jboss:jboss $Jboss_path
#                        /etc/init.d/jboss start > /dev/null
#                        sleep 2
#                  else
#
#                        cd $Jboss_path && rm -rf "$Jboss_path/$App_name.war"
#                        cp $War1 $Jboss_path && chown jboss:jboss $Jboss_path                    
#                        /etc/init.d/jboss start > /dev/null
#                        sleep 2
#                   fi
#             fi
#          fi
#
#          #exit 0           
# 
#}


  JETTY(){

          #业务下线
          #$STATU down > /dev/null

          #备份线上war包，发送新的war包
          #if [ -n $War1 ];then
           if [ ! X${War1} = X ];then

             /usr/bin/killall -9 java > /dev/null

             type1=`echo $War1|awk -F "." '{print $NF}'`


             if [ $type1 = "war" ];then

                   Bak=`ls ${Backup}/${DATE}|wc -l`
                   if [ $Bak -eq 0 ];then

                        cd ${Jetty_path} && mv $App_name* ${Backup}/${DATE}
                        cp $War1 ${Jetty_path}
	                cd /data/jetty/work && rm -rf *
                        /data/jetty/bin/jetty.sh start > /dev/null
	                #sleep 6
	                sleep 40
					tail -n 50 /data/log/jetty/server.log
                   else

                        cd ${Jetty_path} && rm -rf $App_name*
                        cp $War1 ${Jetty_path}
                        cd /data/jetty/work && rm -rf * 
	                /data/jetty/bin/jetty.sh start > /dev/null
                        #sleep 6
                        sleep 40
						tail -n 50 /data/log/jetty/server.log
                   fi

             fi
          fi

          #测试业务状态，host域名绑定本机，正常上线，异常不做处理，去除host绑定
          echo "127.0.0.1  $Domain" >> /etc/hosts
          http_code=$(curl -I -s http://$Domain:8080 -w %{http_code})
      
          #echo "$i" status: ${http_code:9:3}
       
          code=${http_code:9:3}

      
          if [ ${code}X = "200X" -o ${code}X = "302X" -o ${code}X = "301X" -o ${code}X = "304X" ];then 
              echo "$Domain release is : ok"
			  echo "code值:$code."
      
              sed -i '$d' /etc/hosts

              #$STATU up > /dev/nul
               
              exit 0
      
          else
      
              echo  "$Domain release is : error"
              echo "code值:$code."
			  
              sed -i '$d' /etc/hosts

              exit 2
          fi 



	
	#sleep 20 && $STATU up > /dev/nul

}



case $1 in

       jboss)
            JBOSS $2 $3 $4
            ;;
       jetty)
            JETTY $2 $3 $4
            ;;
          *)
            HELP
           ;;
esac
