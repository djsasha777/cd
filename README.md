# IOt project

My iot project with CI/CD integration and running in Kubernetes cluster

Run:

kubectl create ns iotnamespace

kubectl apply -f mongo.yaml

kubectl apply -f app.yaml

port redirecting:

kubectl port-forward --address 172.22.196.117 pod/my-iot-run-6f9b479958-6wqcz 8088:8088
kubectl port-forward --address 172.22.100.107 service/my-monitor-grafana 8091:80
kubectl port-forward --address 172.22.100.107 service/my-service 8088:8088


Testing:

curl -X POST -H "Content-Type: application/json" \
    -d '{"device": 20597, "relay1": false, "relay2": false, "power_mode": 2, "transfer_mode": 7}' \
    192.168.100.31:8088//addrelay/
    
curl -X PUT -H "Content-Type: application/json" \
    -d '{"power_mode": 77, "transfer_mode": 77}' \
    172.22.196.117:8088/setrelay/10025

PCB Layout of device:

<img width="799" alt="2" src="https://user-images.githubusercontent.com/64518378/125844978-dd35f54c-6c29-42c0-bfd5-5ef47cc1e5ab.png">


kubectl logs mongodb-0 -c mongodb