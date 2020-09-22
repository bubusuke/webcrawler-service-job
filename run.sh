#! /bin/bash

# "run.sh" runs main.py intervally.

interval_sec=${JOB_INTERVAL_SEC:-"60"}

while [ true ]
do
    echo "==================================================="
    echo "Start Interval Job. INTERVAL is ${interval_sec} sec."
    echo "==================================================="
    python ./main.py
    if [ $? -ne 0 ]; then
        echo "==================================================="
        echo "Fail to job."
        echo "==================================================="
        exit 1
    fi
    echo "==================================================="
    echo "Success to Job. Sleep ${interval_sec} sec."
    echo "==================================================="
    sleep ${interval_sec}
done
exit 0
