docker build -t server_image -f Dockerfile.server .
docker build -t embassador_image -f Dockerfile.embassador .
docker run -d --name server -p 8080:5000 server_image

docker run -d --name embassador -p 9090:5000 --link server:server embassador_image

curl -X POST http://3.87.24.34:8080/users -d '{"shard_id": "shard1", "user_data": {"username": "user1", "email": "user1@example.com"}}' -H "Content-Type: application/json"
curl http://localhost:8080/users/shard1