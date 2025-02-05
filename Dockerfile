# Инициализация БД
FROM mongo:latest

# Копируем скрипт инициализации DB
COPY init.js /docker-entrypoint-initdb.d/

EXPOSE 27018