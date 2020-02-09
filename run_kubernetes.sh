  
#!/usr/bin/env bash

dockerpath="canfielder/dsba-6190_proj2_docker"

# Run in Docker Hub container with kubernetes
kubectl run dsba-6190_proj2_docker\
    --generator=run-pod/v1\
    --image=$dockerpath\
    --port=80 --labels app=dsba-6190_proj2_docker

# List kubernetes pods
kubectl get pods

# Forward the container port to host
kubectl port-forward dsba-6190_proj2_docker 8000:80