kubectl create secret docker-registry <secret_name> --docker-server=https://index.docker.io/v1/ --docker-username=<user> --docker-password=<password> --docker-email=<email>

kubectl apply -k ./prometheus-snapshots-roles
kubectl apply -f ./prometheus-snapshot-cronjob.yaml 
