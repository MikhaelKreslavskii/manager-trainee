# Инициализация БД
FROM mongo:7.0.16-jammy

WORKDIR /docker-entrypoint-initdb.d
# Копируем скрипт инициализации DB
COPY ./init.js ./

EXPOSE 27017
