* Docker Compose builds a stack of applications to run a complete service. Refer docker-compose.yml
* If any additional packages needs to be installed inside the containers to run certain applications, add it in Dockerfile.
* Use the below command to build the docker 
```
docker compose up --build
```
* open the web UI of airflow once docker is up and running 
``` 
http://localhost:8080
```
