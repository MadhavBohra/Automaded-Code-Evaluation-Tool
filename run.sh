#!/bin/bash

# Create the directory structure
mkdir -p "Output Folder/ResultCases"
mkdir -p "Output Folder/ResultCases_For_Admin"
mkdir -p "Output Folder/Student Submissions"
mkdir -p "Output Folder/Responses"

for set_id in {1..3}; do
    mkdir -p "Output Folder/ResultCases/Set${set_id}"
    mkdir -p "Output Folder/ResultCases_For_Admin/Set${set_id}"
done

for prompt_id in {1..3}; do
    mkdir -p "Output Folder/Responses/SET${prompt_id}"
done

# Run the main.py file
python main.py

echo "Folder structure created successfully and main.py executed."
