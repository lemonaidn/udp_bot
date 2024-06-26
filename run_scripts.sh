#!/bin/bash

# Script to run Python files in sequence

# Ensure the script stops if any command fails
set -e

# Run the Python scripts

echo "Starting openfec_json_downloader.py..."
python openfec_json_downloader.py
echo "openfec_json_downloader.py completed successfully."

echo "Starting fecfile_downloader.py..."
python fecfile_downloader.py
echo "fecfile_downloader.py completed successfully."

echo "Starting extract_desired_data.py..."
python extract_desired_data.py
echo "extract_desired_data.py completed successfully."

echo "Starting twitter_bot.py..."
python tweepy-bots/twitter_bot.py
echo "twitter_bot.py completed successfully."


echo "All scripts completed successfully."