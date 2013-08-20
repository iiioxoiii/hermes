#!/bin/bash

cont=0
cont=`ps -ef | grep "hermes_canta" | grep python | wc | awk ' {print $1}'`
echo $cont
if [ $cont -eq 1 ]
then
echo "ok"
# festival /home/Documents/arduino/apuntador.txt --tts
else
echo "ko"
service hermes_canta start > /dev/null 2> /dev/null < /dev/null &
# service hermes_canta start
fi
