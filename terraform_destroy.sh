#! bin/bash

cd kubernetes
kubectl delete all --all
kubectl delete configmap --all
kubectl delete ingress --all
kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.47.0/deploy/static/provider/aws/deploy.yaml

cd ..

cd amazon_eks
terraform destroy --auto-approve