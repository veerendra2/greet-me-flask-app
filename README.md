# Greet Me
A simple Flask application that greets you according to the time of day.

> :information_source: A demo app to demonstrate CI/CD pipeline for deployment on Kubernetes (Minikube).

:diamond_shape_with_a_dot_inside: _**Refer :books:[Gitbook Documentation](https://dust6765.gitbook.io/greet-me-app-documentation/):books: for more information.**_

## :arrow_forward: Run Locally
```bash
$ git clone git@github.com:veerendra2/greet-me-flask-app.git
$ cd greet-me-flask-app
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
