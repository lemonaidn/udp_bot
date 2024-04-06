#!/bin/bash

# Script to run Python files in sequence

# Ensure the script stops if any command fails
set -e

# Run the Python scripts
echo "Starting openfec_downloader.py..."
python openfec_downloader.py
echo "openfec_downloader.py completed successfully."

echo "Starting fec_downloader.py..."
python fec_downloader.py
echo "fec_downloader.py completed successfully."

echo "Starting extract_desired_data.py..."
python extract_desired_data.py
echo "extract_desired_data.py completed successfully."

echo "All scripts completed successfully."