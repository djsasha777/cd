# IOt project

My iot project with CI/CD integration and running in Kubernetes cluster

KUBE running:

kubectl create ns open5gs

kubectl apply -f IOT/

run Docker app in osx command:
/Applications/Docker.app/Contents/MacOS/Docker


add port redirecting in xiaomi router:
iptables -t nat -A PREROUTING -d 172.22.7.185 -p tcp --dport 6060 -j DNAT --to-destination 192.168.1.187:6060

PCB Layout of device:

<img width="799" alt="2" src="https://user-images.githubusercontent.com/64518378/125844978-dd35f54c-6c29-42c0-bfd5-5ef47cc1e5ab.png">

