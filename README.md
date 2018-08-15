# kubernetes-basic

# Useful Commands:

```
kubectl cluster-info
kubectl get services
kubectl get deployments
kubectl get pods
kubectl get ing
kubectl get hpa
```

# Running Benchmarks using ab

```
ab -c 100 -n 10000 http://192.168.99.100/get/foo
```

# Solution:

```
Using a custom python application for stateless application and redis as backend stateful application.
Python application connects to redis using its service dns name "redis.default".
Created an ingress on top of python application for load balancing.
Created an autoscalar for spinning up additional frontend pods.
```
