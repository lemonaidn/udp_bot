import requests
import csv
import time

# Path to the file containing the URLs
urls_file_path = 'csv_urls.csv'
# Path to the output file
output_file_path = 'csv_output.csv'

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

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

# Open the output file
with open(output_file_path, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Loop through each URL
    for url in urls:
        response = make_request(url)
        if response:
            # Decode the content and split it into lines
            content = response.content.decode('utf-8')
            lines = content.splitlines()
            # Extract the third line
            third_line = lines[2] if len(lines) > 2 else None
            # Write the third line to the output file
            if third_line:
                reader = csv.reader([third_line])
                for row in reader:
                    writer.writerow(row)
        # Wait a bit between requests to respect the server's rate limit
        time.sleep(1)  # Wait 1 second before the next request
