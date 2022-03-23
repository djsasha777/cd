# IOt project

My iot project with CI/CD integration and running in Kubernetes cluster

helm install mymongo --values helm_config_mongo.yaml bitnami/mongodb

port redirecting:


kubectl port-forward --address 172.22.140.195 service/my-monitor-grafana 8091:80

kubectl port-forward --address 172.22.140.195 service/my-service 8088:8088

kubectl port-forward --address 172.22.140.195 service/mongo-express-service 8081:8081

Testing:

curl -X POST -H "Content-Type: application/json" \
    -d '{"device": 20597, "relay1": false, "relay2": false, "power_mode": 2, "transfer_mode": 7}' \
    172.22.7.185:8088//addrelay/
    
curl -X PUT -H "Content-Type: application/json" \
    -d '{"power_mode": 77, "transfer_mode": 77}' \
    172.22.196.117:8088/setrelay/10025

kubectl logs mongodb-0 -c mongodb


iptables -t nat -A PREROUTING -d 172.22.7.185 -p tcp --dport 8088 -j DNAT --to-destination 192.168.1.113:8088



!!!!!!!!
for kubernetes dashboard(https)
iptables -t nat -A PREROUTING -d 172.22.7.185 -p tcp --dport 1100 -j DNAT --to-destination 192.168.1.111:443
!!!!!!!!!! https://172.22.7.185:1100



helm repo add metallb https://metallb.github.io/metallb

helm install metallb metallb/metallb -f helm_values_metal.yaml