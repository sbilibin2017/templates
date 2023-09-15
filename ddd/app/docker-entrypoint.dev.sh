#!/bin/bash

echo "Waiting for cache ..."
while ! nc -z cache 6379; do
  sleep 1
done
echo "Cache started"

echo "Waiting for db ..."
while ! nc -z db 9200; do
  sleep 1
done
echo "Database started"

uvicorn app:app --host 0.0.0.0 --port 8000 --reload