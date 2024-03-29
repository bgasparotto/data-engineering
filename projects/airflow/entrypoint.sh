#!/bin/bash

echo "Setting database up"
airflow db init

echo "Creating admin user"
airflow users create -u admin -p admin -r Admin -f Bruno -l Gasparotto -e bruno.m.gasparotto@gmail.com

echo "Cleaning previous storage migration states (if any)"
airflow tasks clear storage -y

echo "Starting webserver"
airflow webserver --port 8080 &
sleep 5 # wait until the webserver has written its logs so the output is clearer

echo "Starting scheduler"
airflow scheduler
