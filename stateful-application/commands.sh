kubectl create configmap redis-config-map --from-file=redis-config
kubectl create -f 01-pvc
kubectl create -f 02-redis
