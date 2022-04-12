#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $1 5432; do
  sleep 0.1
done

rm -rf celery_logs/*

echo "PostgreSQL started"
