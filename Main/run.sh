#!/bin/bash

required_elements=("functions" "main.py" "menues" "utils")

for element in "${required_elements[@]}"; do
    if [[ ! -f "$element" && ! -d "$element" ]]; then
        echo "Files '$file' is missing. Please make sure all required files are present."
        exit 1
    fi
done
python3 main.py

# Author: Christian Rystad/antig0ne

