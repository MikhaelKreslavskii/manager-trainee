# Инициализация БД
FROM mongo:latest
WORKDIR /docker-entrypoint-initdb.d
# Копируем скрипт инициализации DB
COPY init.js /docker-entrypoint-initdb.d/

EXPOSE 27018