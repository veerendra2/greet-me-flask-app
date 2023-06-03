# Greet Me app
A simple flask application greets clients depending on time.

## Abstract
> First, create a very simple application that greets you according to the time of day. “Good Morning, Good Afternoon, Good Evening”. It should run in a Docker container and provide the service on port 8080. Don’t forget to write a couple of tests.
>
> Now that you've warmed up, we’ll tell you the real challenge.
>
> Since of course you want to be able to test and deploy your very complicated application in a fast and reliable way, we kindly ask you to create a CI/CD pipeline.
>
> Use a local Kubernetes cluster (Minikube, kind, rancher,....) to deploy your application.

[Gitbook Documentation](https://dust6765.gitbook.io/greet-me-app-documentation/)

### Run locally
```bash
$ cd src/greet_me
$ python3 greet_me.py
INFO:Serving on http://0.0.0.0:8080
```
