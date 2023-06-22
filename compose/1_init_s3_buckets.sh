#!/bin/bash

awslocal s3 mb s3://national-grid-eso
awslocal s3 cp /datasets/national_grid_demand/ s3://national-grid-eso/demand --recursive

awslocal s3 mb s3://datalake
