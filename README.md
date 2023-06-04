# Greet Me
A simple flask application that greets you according to the time of day.

:diamond_shape_with_a_dot_inside: _**Refer :books:[Gitbook Documentation](https://dust6765.gitbook.io/greet-me-app-documentation/):books: for more info.**_

## :information_source: Abstract
> First, create a very simple application that greets you according to the time of day. “Good Morning, Good Afternoon, Good Evening”. It should run in a Docker container and provide the service on port 8080. Don’t forget to write a couple of tests.
>
> Now that you've warmed up, we’ll tell you the real challenge.
>
> Since of course you want to be able to test and deploy your very complicated application in a fast and reliable way, we kindly ask you to create a CI/CD pipeline.
>
> Use a local Kubernetes cluster (Minikube, kind, rancher,....) to deploy your application.

## :arrow_forward: Run Locally
```bash
$ git clone git@github.com:veerendra2/greet-me-flask-app.git

$ python3 src/greet_me/greet_me.py
INFO:Serving on http://0.0.0.0:8080

# install as pypi package
$ pip3 install -e .

# run cli
$ greet_me
INFO:Serving on http://0.0.0.0:8080

# uninstall pypi package
$ pip3 uninstall greet_me
```
