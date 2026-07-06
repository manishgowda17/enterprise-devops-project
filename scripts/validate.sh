#!/bin/bash

echo "================================="
echo " Running Project Validation"
echo "================================="

echo "Checking project files..."

required_files=(
    "app/app.py"
    "app/requirements.txt"
    "docker/Dockerfile"
    "docker/docker-compose.yml"
)

for file in "${required_files[@]}"
do
    if [ ! -f "$file" ]; then
        echo "ERROR: Missing $file"
        exit 1
    fi
done

echo "All required files exist."

echo "Checking Python syntax..."

python3 -m py_compile app/app.py

if [ $? -eq 0 ]; then
    echo "Python syntax is valid."
else
    echo "Python syntax error."
    exit 1
fi

echo "Validation Successful."
