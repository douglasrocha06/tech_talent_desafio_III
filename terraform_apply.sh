#! bin/bash

cd amazon_eks
terraform init
terraform apply --auto-approve

cd ..

cd kubernetes
aws eks update-kubeconfig --name eks-cluster-dl
kubectl apply -f eks_ingress.yaml
kubectl apply -f deploy.yaml
kubectl apply -f eks_configmap.yaml
kubectl apply -f eks_deployments.yaml
kubectl apply -f eks_clusterIP.yaml

kubectl get svc --all-namespaces