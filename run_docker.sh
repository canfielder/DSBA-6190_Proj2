#!/usr/bin/env bash

# Build image
docker build --tag=dsba-6190_proj2_docker .

# List docker images
docker image ls

# Run flask app
docker run --rm -d -p 8080:8080 dsba-6190_proj2_docker

docker ps

curl http://localhost:8080