#!/bin/sh

RETRIES=5

until psql -U test-user -d test-db -f ./opt/setup/setup.sql|| [ $RETRIES -eq 0 ]; 
do   echo "Waiting for postgres server to start, $((RETRIES)) remaining attempts..."   
RETRIES=$((RETRIES-=1))   
sleep 1 
done