import requests
import csv
import time
import os

# Path to the file containing the FEC URLs
urls_file_path = 'fec_urls.csv'
# Directory to save the downloaded FEC files
fec_files_dir = 'fec_files'

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Ensure the directory for FEC files exists
os.makedirs(fec_files_dir, exist_ok=True)

# Function to make a request with retries
def make_request(url, num_retries=3):
    for i in range(num_retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error for {url}: {e}, attempt {i+1} of {num_retries}")
            time.sleep(10)  # Wait 10 seconds before retrying
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error for {url}: {e}, attempt {i+1} of {num_retries}")
            break  # No retry for HTTP errors like 404, 403 etc.
        except Exception as e:
            print(f"Unexpected error for {url}: {e}, attempt {i+1} of {num_retries}")
    return None

# Read the URLs from the file
with open(urls_file_path, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

# Loop through each URL to download FEC files
for url in urls:
    response = make_request(url)
    if response:
        # Get the filename from the URL to save it locally
        filename = url.split('/')[-1]
        path_to_save = os.path.join(fec_files_dir, filename)

        # Save the content to a file
        with open(path_to_save, 'wb') as fec_file:
            fec_file.write(response.content)

        print(f"Downloaded and saved {filename}")

    # Wait a bit between requests to respect the server's rate limit
    time.sleep(1)  # Wait 1 second before the next request
