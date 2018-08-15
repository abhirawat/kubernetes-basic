#!/bin/bash

## Application built using following commands
#docker build -t rawat/stateless-application .
#sudo docker tag rawat/stateless-application:latest rawat/stateless-application:1.0
#docker push rawat/stateless-application:1.0

kubectl create -f 01-app
kubectl create -f 02-app-ing
kubectl create -f 03-autoscale
