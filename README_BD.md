### Запуск Docker-compose
1. Запускаем сборку контейнера
docker-compose up -d
2. Подключение к БД \
Через консоль: \
``` mongosh "mongodb://admin:password@localhost:27017" ``` \
ИЛИ \
``` docker exec -it mongo-container mongosh "mongodb://admin:password@localhost:27017"``` \
Через Python-> \
``` client = MongoClient("mongodb://admin:secret@localhost:27017") ```
3. Остановить контейнер \
```docker-compose down```