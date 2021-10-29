# WordPlay
This project consists of a Flask-based application which allows you to retrieve information about English words. In the backend, it uses APIs based one 'WordsAPI' (https://rapidapi.com/dpventures/api/wordsapi/).

To run the app locally:

1. In Docker:
- Build a docker image from the available Dockerfile
    `docker build -t wordplay:latest -f Dockerfile .`

- Run the docker image:
    `docker run -p 5000:5000 -d wordplay:latest`

You can now use the app by browsing to `localhost:5000`

2. In Kubernetes: \
    [Note: To run in Kubernetes, make sure you have a local Kubernetes cluster installed, for example via minikube or one bundled within Docker Desktop(or any other). This can also be run in a Kubernetes cluster elsewhere, for instance in the cloud, with little to no changes to the spec file(kubernetes.yaml)] \

- If not already done so, build a docker image from the available Dockerfile
    `docker build -t wordplay:latest -f Dockerfile .`

- Run the following kubectl command
    `kubectl apply -f kubernetes.yaml`

This will create a deployment and a service of type "Load balancer", which can then be accessed on `localhost:5000` (or any other port specified in the spec file)

