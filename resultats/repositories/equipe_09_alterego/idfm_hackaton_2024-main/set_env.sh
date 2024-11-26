#!/bin/bash

# List of .env files
env_files=("deployment.env" "secrets.env")

# Function to load environment variables from .env files
load_env_vars() {
    for env_file in "${env_files[@]}"; do
        # Check if the file exists
        if [ -f "$env_file" ]; then
            # Read each line in the file
            while IFS= read -r line || [[ -n "$line" ]]; do
                # Skip empty lines and lines that start with a hash (#)
                if [[ ! $line =~ ^# && $line ]]; then
                    # Export the variable by evaluating the line
                    export "$line"
                fi
            done < "$env_file"
        else
            echo "The file $env_file does not exist in $(pwd)."
        fi
    done
}

# Load environment variables
load_env_vars
