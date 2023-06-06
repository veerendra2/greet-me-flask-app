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
    ├── prod
    │   ├── kustomization.yaml
    │   ├── namespace.yml
    │   ├── patch-image.yaml
    │   └── patch-ingress.yaml
    └── staging
        ├── kustomization.yaml
        ├── namespace.yml
        ├── patch-image.yaml
        └── patch-ingress.yaml

4 directories, 15 files
```