# Final Project Configuration and Usage Documentation #

## Configuration ##

Note: Proceed with initial config in test environment

1) Initialize redis-db yaml files to set redis-service ip address (performed in finalProject2.0/kube/test/ directory):

```bash
[axentom@isp02 test]$ kubectl apply -f axentom-test-redis-pvc.yml
[axentom@isp02 test]$ kubectl apply -f axentom-test-redis-service.yml
```

2) Note redis-service ip address in 'CLUSTER-IP' column:

```bash
[axentom@isp02 test]$ kubectl get services -o wide
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE   SELECTOR
axentom-test-redis-service   ClusterIP   10.110.179.174   <none>        6379/TCP   8h    app=axentom-test-redis
```

3) Enter jobs.py with text editor of choice and set ip address string variable found on line 6 as redis-service ip

(Example shown with vi, jobs.py file found in finalProject2.0/source/ directory):

```bash
[axentom@isp02 source]$ vi jobs.py
```

jobs.py file snippet shown below:
```bash
import uuid
from hotqueue import HotQueue
from redis import StrictRedis
import os

rd_ip = '10.110.179.174'
...
```


4) Load data. Accepted data is in JSON format. CSV-to-JSON converter script is provided as finalProject2.0/source/csv2json.py.

5) Build Docker images from Dockerfiles found in finalProject2.0/docker/ directory

(Example build commands must be completed from finalProject2.0/source/ directory)

```bash
[axentom@isp02 source]$ docker build -f ../docker/Dockerfile.api -t axentom/final-project-api:1.0 .
[axentom@isp02 source]$ docker build -f ../docker/Dockerfile.wrk -t axentom/final-project-wrk:1.0 .
```

Please note argument for -t flag should be changed to user tag in order to be able to push to DockerHub.

-t flag takes argument in the form: `<dockerhub-username>/<repo>:<version>`

6) Push Docker images to DockerHub (push argument must match -t arguments used in previous step)

```bash
[axentom@isp02 source]$ docker push axentom/final-project-api:1.0
[axentom@isp02 source]$ docker push axentom/final-project-wrk:1.0
```

7) Configure image selection for Kubernetes deployment YAML files as pictured below:

finalProject2.0/kube/test/axentom-test-flask-deployment.yml:
```bash
...
    spec:
      containers:
        - name: axentom-test-flask-pod
          imagePullPolicy: Always
          image: axentom/final-project-api:1.0
...
```

finalProject2.0/kube/test/axentom-test-worker-deployment.yml:
```bash
...
    spec:
      containers:
        - name: axentom-test-worker-pod
          imagePullPolicy: Always
          image: axentom/final-project-wrk:1.0
...
```

Please note that these image: arguments must match -t arguments pushed to DockerHub

8) Complete Kubernetes deployment in finalProject2.0/kube/test/ directory:

```bash
[axentom@isp02 test]$ kubectl apply -f axentom-test-redis-deployment.yml
[axentom@isp02 test]$ kubectl apply -f axentom-test-flask-deployment.yml
[axentom@isp02 test]$ kubectl apply -f axentom-test-flask-service.yml
[axentom@isp02 test]$ kubectl apply -f axentom-test-worker-deployment.yml
```

9) Review output and then repeat for prod environment

Note: Redis-DB data initialization completed in User Workflow Steps 1-5

## User Guide ##

Example user deployment provided with finalProject2.0/kube/test/axentom-pythonDebug-deployment.yml

### User Workflow ###

1) Deploy example user deployment:
[axentom@isp02 test]$ kubectl apply -f axentom-pythonDebug-deployment.yml

2) Note example user pod name:

```bash
[axentom@isp02 test]$ kubectl get pods
```

Example output shown below (note NAME):
```bash
NAME                                              READY   STATUS    RESTARTS   AGE
...
py-debug-deployment-8f9458db-j2k57                1/1     Running   0          9h
py-debug-deployment-8f9458db-kkc2v                1/1     Running   0          9h
```

3) Exec into previously noted pod:

```bash
[axentom@isp02 test]$ kubectl -it py-debug-deployment-8f9458db-j2k57 -- /bin/bash
```

4) Note flask-service ip address:

```bash
[axentom@isp02 test]$ kubectl get services
```

Example output shown below (note CLUSTER-IP):
```bash
NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
axentom-test-flask-service   ClusterIP   10.101.149.233   <none>        5000/TCP   9h
```

5) Run user commands by curling to flask-service-ip at port 5000

IMPORTANT: first route must hit the /loaddata route in order to initialize Redis-DB with data from data.json

```bash
curl 10.101.149.233:5000/loaddata
```

### Other Available User Commands ###

1) Output all data

```bash
curl 10.101.149.233:5000/get
``` 
2) Create - Create entry

Arguments:
`id_no` : Animal ID to search by
`name` : Animal name
`datetime` : Date and Time of outcome occurrence in format: "MM/DD/YYYY HH:MM:SS XM"
`monthyear` : Month and Year of outcome occurrence in format: "MM/DD/YYYY HH:MM:SS XM"
`dob` : Date of Birth in format: "MM/DD/YYYY"
`outcome_type` : Type of outcome, example: "Adoption"
`outcome_subtype` : Subtype of outcome
`animal_type` : Species
`sex` : Animal sex at outcome occurrence
`age` : Animal age at outcome occurrence
`breed` : Animal breed
`color` : Animal color

```bash
curl 10.101.149.233:5000//create/<id_no>/<name>/<datetime>/<monthyear>/<dob>/<outcome_type>/<outcome_subtype>/<animal_type>/<sex>/<age>/<breed>/<color>
```

3) Read - Output entry by Animal ID

Arguments:
`id_no` : Animal ID to search by

```bash
curl 10.101.149.233:5000/read/<id_no>
```

4) Update - Edit value at designated key for entry by Animal ID

Arguments:
`id_no` : Animal ID to search by
`key` : Key value for desired update value
`new_value` : Desired update value

```bash
curl 10.101.149.233:5000/read/<id_no>/update/<key>/<new_value>
```

5) Destroy - Delete entry by Animal ID

Arguments:
`id_no` : Animal ID to search by

```bash
curl 10.101.149.233:5000/delete/<id_no>
```

6) Job - Create bar plot of adoption ages of adopted animals

(Output in PNG format, sent to finalProject2.0/sources/ directory)

```bash
curl 10.101.149.233:5000/jobs -X POST -d '{"start": "start","end": "end"}'
```
