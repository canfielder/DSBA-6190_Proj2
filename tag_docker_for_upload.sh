#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes this is built
#docker build --tag=dsba-6190_proj2_docker .


dockerpath="canfielder/dsba-6190_proj2_docker"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag dsba-6190_proj2_docker $dockerpath

# Push Image
docker image push $dockerpath 