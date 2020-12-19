docker build -t test_task:v0.1 .
docker images

docker stop $(docker ps -aq)

Remove all containers

docker rm $(docker ps -aq)


