#!/bin/bash

echo "Setting database up"
airflow db init

echo "Creating admin user"
airflow users create -u admin -p admin -r Admin -f Bruno -l Gasparotto -e bruno.m.gasparotto@gmail.com

echo "Starting webserver"
airflow webserver --port 8080 &
sleep 5 # wait until the webserver has written its logs

echo "Starting scheduler"
airflow scheduler
