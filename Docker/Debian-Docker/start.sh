#!/usr/bin/env bash

if [[ -v QUESTIONATOR_TOKEN ]]; then
    echo "Questionator_Token=${QUESTIONATOR_TOKEN}" >> /Questionator/Bot/.env
else
    echo "Missing Questionator's bot token! QUESTIONATOR_TOKEN environment variable is not set."
    exit 1;
fi

# Testing bot token
# Not needed in production
if [[ -v QUESTIONATOR_DEV_TOKEN ]]; then
    echo "Questionator_Dev_Token=${QUESTIONATOR_DEV_TOKEN}" >> /Questionator/Bot/.env
fi 

# PostgreSQL Credentials
if [[ -v POSTGRES_PASSWORD ]]; then
    echo "Postgres_Password=${POSTGRES_PASSWORD}" >> /Questionator/Bot/.env
else
    echo "Missing POSTGRES_PASSWORD! Postgres_Password environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_USER ]]; then
    echo "Postgres_User=${POSTGRES_USER}" >> /Questionator/Bot/.env
else
    echo "Missing POSTGRES_USER! Postgres_User environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_DB ]]; then
    echo "Postgres_DB=${POSTGRES_DB}" >> /Questionator/Bot/.env
else
    echo "Missing POSTGRES_DB! Postgres_DB environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_HOST ]]; then
    echo "Postgres_Host=${POSTGRES_HOST}" >> /Questionator/Bot/.env
else
    echo "Missing POSTGRES_HOST! Postgres_Host environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_PORT ]]; then
    echo "Postgres_Port=${POSTGRES_PORT}" >> /Questionator/Bot/.env
else
    echo "Missing POSTGRES_PORT! Postgres_Port environment variable is not set."
    exit 1;
fi

# Redis Credentials
if [[ -v REDIS_HOST ]]; then
    echo "Redis_Host=${REDIS_HOST}" >> /Questionator/Bot/.env
else
    echo "Missing REDIS_HOST! Redis_Host environment variable is not set."
    exit 1;
fi

if [[ -v REDIS_PORT ]]; then
    echo "Redis_Port=${REDIS_PORT}" >> /Questionator/Bot/.env
else
    echo "Missing REDIS_PORT! Redis_Port environment variable is not set."
    exit 1;
fi


exec python3 /Questionator/Bot/main.py