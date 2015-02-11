#!/bin/bash

Home=$(cd $(dirname $0);pwd)
Date=`date +%Y-%m-%d`
Time=`date +"%Y-%m-%d%H:%M"`
Appname=$1
Kive_file=$2

Kive_path="/data/$Appname/kiev/app"
Backup="/data/kiev_backup"
Pid="/data/$Appname/kiev/bin/kiev.pid"
Bin="/data/$Appname/kiev/bin/kiev.sh"
Kive_log="/data/$Appname/kiev/logs/kiev.out"

Ipaddr=`/sbin/ifconfig |grep -A2 "eth0" |awk -F':' '{if($2 ~ /^[0-9][0-9][0-9]\./)print $2}' |cut -d" " -f 1`

if [ ! -d ${Backup}/$Appname/${Date} ];then

        mkdir -p $Backup/$Appname/$Date
        $Bin stop
        mv $Kive_path/* $Backup/$Appname/$Date
        unzip $Kive_file -d $Kive_path
        [ -f $Pid ] && $Bin stop
	sleep 2
        $Bin start
     else   
       mkdir -p $Backup/$Appname/$Date/"$Time"
       $Bin stop
       sleep 3
       [ -f $Pid ] && $Bin stop
       #mkdir -p $Backup/$Appname/"$Date-$Time"
       mv $Kive_path/* $Backup/$Appname/$Date/"$Time"
       unzip $Kive_file -d $Kive_path
       [ ! -f $Pid ] && $Bin start
#       $Bin start
       sleep 3
fi


   count=`ps -ef|grep /data/$Appname|grep -v grep|wc -l`
   if [ $count -ge 1 ];then

       echo "$Appname Kive start ok!"
       tail -n 50 $Kive_log
   else
       echo "$Appname not start,please find problemp!" 
       tail -n 50 $Kive_log
   fi
