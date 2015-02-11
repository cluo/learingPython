#!/bin/bash


Home=$(cd $(dirname $0); pwd)
#DATE=`date "+%Y-%m-%d %T"`
DATE=`date "+%Y-%m-%d-%H-%M"`
Log="/tmp/static.log"
Ipaddr=`/sbin/ifconfig |grep -A2 "eth0" |awk -F':' '{if($2 ~ /^[0-9][0-9][0-9]\./)print $2}' |cut -d" " -f 1`
Backup="/data/static-backup"
Static_path="/data/static/"
Transfer="/data/transfer"
Source="/data/static/static/resources"
#App_name=$2
Static_war=$1


HELP(){

       echo "USAG: 详细信息如下
             $PATH_SH/static.sh warfile
             1、 文件路径"
}


if [ $# -ne 1 ];then

     HELP
     exit 0
 
fi



if [ ! -d $Backup/$DATE ];then

      mkdir -p $Backup/$DATE

fi

if [ ! -d $Backup/$Transfer ];then

      mkdir -p $Backup/$Transfer
      unzip $Static_war -d  $Backup/$Transfer
 else
      cd  $Backup/$Transfer && rm -rf *
      unzip $Static_war -d  $Backup/$Transfer

fi


#for i in `ls -l $Backup/$Transfer/resources|awk '{print $9}'`
for i in `ls -l $Backup/$Transfer/resources|awk '{if (NR>1) print $NF}'`
do


      if [ -d ${Source}/$i ];then

          cp -r  ${Source}/$i $Backup/$DATE
          sleep 2
          \cp -r $Backup/$Transfer/resources/$i ${Source}  
          
           #> $Home/static/${Ipaddr}.log
           echo "$DATE:Static 发布成功!"
          

        else

          \cp -r $Backup/$Transfer/resources/$i ${Source}  
        
           #> $Home/1og/${Ipaddr}.log
           #echo "$DATE:Static 发布成功!" >> $Home/log/${Ipaddr}.log        
           echo "$DATE:Static 发布成功!"

      fi
               
 
done
