FROM duffn/python-poetry:3.9.18-slim as build
WORKDIR /app
COPY ./ ./



RUN chown 10000:10001 -R /app

USER nonroot

ENTRYPOINT ["python", "__init__.py"]
