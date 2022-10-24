#!/usr/bin/env bash

if [[ -v QUESTIONATOR_TOKEN ]]; then
    echo "Questionator_Token=${QUESTIONATOR_TOKEN}" >> /Questionator/Bot/.env
else
    echo "Missing Questionator's bot token! QUESTIONATOR_TOKEN environment variable is not set."
    exit 1;
fi

# Testing bot token
# Not needed in production
if [[ -v DEV_BOT_TOKEN ]]; then
    echo "Questionator_Dev_Token=${DEV_BOT_TOKEN}" >> /Questionator/Bot/.env
fi 

exec python3 /Questionator/Bot/main.py