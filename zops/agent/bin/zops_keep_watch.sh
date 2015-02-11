#!/bin/bash

ulimit -SHn 65535

pid_exists () {
    # This is better than "kill -0" because it doesn't require permission to
    # send a signal (so daemon_status in particular works as non-root).
    test -d /proc/"$1"
}

daemon_is_running () {
    proc=$1
    proc_pids=$(pgrep -f ${proc})
    test -z ${proc_pids} && return 1
    for pid in ${proc_pids}
    do
        test -n "$pid" && pid_exists "$pid"
    done
} >/dev/null 2>&1
# get bin dir
BIN_DIR=$(cd `dirname $0`; pwd)
cd $BIN_DIR

process_list=(ops_watch/watchdog.py)

function start(){
    cd ..
    for proc in ${process_list[@]}
    do
        if daemon_is_running ${proc}; then
            if [ X"$(date +'%M%S')" == X"0000" ]
            then
                echo -e "$(date +'%Y-%m-%d %H:%M:%S')\t${proc} is running"
            fi
            continue
        fi
        nohup python ${proc} > /var/log/zops_keep_watch 2>&1 &
        daemonpid=$!
        sleep 1
        if kill -0 $daemonpid ; then
            echo -e "start ${proc#*/}\t\t[\033[0;32;1mOK\033[0m]"
        else
            wait $daemonpid; daemonexit=$?
            echo -e "start ${proc#*/}\t\t[\033[0;31;1mFAILED\033[0m]"
            cat /var/log/zops_keep_watch
            echo -e "start zops_keep_watch\t\t[\033[0;31;1mFAILED\033[0m]"
            return 1
        fi
    done
}

start