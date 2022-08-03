# Testing API:


    
curl -X PUT -H "Content-Type: application/json" -d '{"device": 222, "upsensor": 0, "downsensor": 0, "flowsensor": 4, "relay": 0, "workmode": 1, "errors": "no err"}' http://localhost:8444/setsensor/222


curl -X POST -H "Content-Type: application/json" -d '{"device": 222, "upsensor": false, "downsensor": false, "flowsensor": 4, "relay": true, "workmode": 1, "errors": "no err"}' http://localhost:8444/addsensor/