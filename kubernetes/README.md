# Deployment on Kubernetes
Kustomize overlay structure
```bash
$ tree .
.
├── README.md
├── base
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── kustomization.yaml
│   ├── service.yaml
│   └── serviceaccount.yaml
└── stages
    ├── dev
    │   └── kustomization.yaml
    └── prod
        └── kustomization.yaml

4 directories, 9 files
```