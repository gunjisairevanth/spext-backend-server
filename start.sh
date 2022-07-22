#!/bin/bash
# echo "Starting Nginx"
# mkdir /run/nginx
# nginx

echo "Starting python"
# ls
gunicorn --bind 0.0.0.0:5000 run:app