docker build -t stateless-application .
# Test using docker run -it --rm --name stateless-application stateless-application
sudo docker tag stateless-application:latest stateless-application:1.0
docker push rawat/stateless-application
