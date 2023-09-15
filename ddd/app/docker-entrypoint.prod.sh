#!/bin/bash

echo "Waiting for cache ..."
while ! nc -z ${DOCKER_CACHE_HOST} ${CACHE_PORT}; do
  sleep 1
done
echo "Cache started"

echo "Waiting for db ..."
while ! nc -z ${DOCKER_DB_HOST} ${DB_PORT}; do
  sleep 1
done
echo "Database started"

gunicorn app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:${APP_PORT}