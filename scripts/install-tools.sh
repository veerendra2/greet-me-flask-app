#!/bin/bash

# Author: Veerendra Kakumanu
# Description: Installs tools
# Refer documentation for more info: https://dust6765.gitbook.io/greet-me-app-documentation/

# for AMD64 / x86_64
[ $(uname -m) = x86_64 ] \
  && echo "[*] Download kind and kubectl binary" \
  && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-amd64 \
  && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# for ARM64
[ $(uname -m) = aarch64 ] \
  && echo "[*] Download kind and kubectl binary" \
  && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-arm64 \
  && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"

# kustomize
curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash

$ chmod +x {./kind,./kubectl,./kustomize}
$ sudo mv ./kind /usr/local/bin/kind
$ sudo mv ./kubectl /usr/local/bin/kubectl
$ sudo mv ./kustomize /usr/local/bin/
