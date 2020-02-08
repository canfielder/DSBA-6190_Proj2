#!/usr/bin/env bash

# Build image
docker build --tag=dsba-6190_proj2_docker .

# List docker images
docker image ls

# Run flask app
docker run -p 8000:80 dsba-6190_proj2_docker