#!/bin/sh

SLEEP_SEC=1800
LOOP_MAX=16560

COUNT=0
while [ $COUNT -lt $LOOP_MAX ]
do
  
  python ../src/autoBuy.py
  
  sleep ${SLEEP_SEC}
done
