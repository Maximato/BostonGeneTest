docker build --tag signatures-restapi .
docker run -d --name sign -p 80:80 signatures-restapi
