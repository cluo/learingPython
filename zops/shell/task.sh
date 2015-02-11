#!/bin/bash

Home=$(cd $(dirname $0);pwd)
DATE=`date +%Y-%m-%d`
Time=`date +"%Y-%m-%d%H:%M"`
Task_path="/data/launcher/task/app"
Backup="/data/task_backup"
Start="/data/launcher/task/bin/start.sh"
Stop="/data/launcher/task/bin/stop.sh"
Ipaddr=`/sbin/ifconfig |grep -A2 "eth0" |awk -F':' '{if($2 ~ /^[0-9][0-9][0-9]\./)print $2}' |cut -d" " -f 1`
Appname=$1
Task_file=$2

#Task path /data/launcher/task 固定目录必须存在，否则手动确认,这里不做判断!

   if [ ! -d $Backup/$Appname/$DATE ];then

        mkdir -p $Backup/$Appname/$DATE
        $Stop
        mv /data/launcher/task/app/* $Backup/$Appname/$DATE
        unzip $Task_file -d $Task_path
        $Start

   else 
       $Stop
       mkdir -p $Backup/$Appname/$DATE/"$Time"
       mv /data/launcher/task/app/* $Backup/$Appname/$DATE/"$Time"
       unzip $Task_file -d $Task_path
       $Start
   fi


   count=`ps -ef|grep task|grep -v grep|wc -l`
   if [ $count -ge 2 ];then
       
        echo "$Appname task start ok!"
        
   else
       echo "$Appname not start,please find problemp!" 
   fi 

 
