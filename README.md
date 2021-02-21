### PS4Joyscout-microservice server on gRPC
### Using python3.8, Dockerized

#### Implements Binary Search to retrieve the last page on the PlayStation Store.
#### Facilitates web scraping by introducing a tad of certainty.

##Usage
```
cd ps4grpcmicroservice-glp
docker build . -t lastpage
docker container run --detach --publish 50051:50051 --name lastpage lastpage
```