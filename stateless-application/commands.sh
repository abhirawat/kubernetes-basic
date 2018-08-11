docker build -t rawat/stateless-application .
# Test using docker run -it --rm --name stateless-application stateless-application
sudo docker tag rawat/stateless-application:latest rawat/stateless-application:1.0
docker push rawat/stateless-application:1.0
