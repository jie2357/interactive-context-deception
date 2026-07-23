#!/bin/bash

echo "Starting deployment..."

echo "Loading production profile..."

export AWS_PROFILE=production

docker compose up -d

echo "Deployment completed."

echo "For credential configuration see:"

echo "config/aws.conf"