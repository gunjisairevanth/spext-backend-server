#!/bin/bash
echo "Starting Nginx"
mkdir /run/nginx
nginx

echo "Starting python"
ls
python3 run.py