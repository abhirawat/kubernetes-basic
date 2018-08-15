# Kubernetes Basic Setup/Solution:

```
Using a custom python application for stateless application and redis as backend stateful application.
Python application connects to redis using its service dns name "redis.default".
Created an ingress on top of python application for load balancing.
Created an autoscaler for spinning up additional frontend pods.
```

## Stateful App
```
All config and instructions present in directory stateful-application.
Using default kubernetes redis-2.8 container.
Supplying own config along with a persistent volume for data to stay across container restarts.
```

## Stateless App
```
Application code and all config along with instructions present in directory stateless-application.
Using custom docker container pushed to namespace rawat/ in dockerhub.
Added "interview.travix.com" entry in /etc/hosts to point to clusters external ip.
```


### Running Benchmarks using ab

```
ab -c 100 -n 10000 http://192.168.99.100/get/foo
```

### Useful Commands:

```
minikube ip
kubectl cluster-info
kubectl get services
kubectl get deployments
kubectl get pods
kubectl get ing
kubectl get hpa
```
