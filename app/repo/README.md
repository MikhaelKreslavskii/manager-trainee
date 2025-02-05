docker build -t mongo-image .
docker run -d -p 27017:27017 --name mongo-container mongo-image

# Connect via console - optional
docker exec -it mongo-container mongosh