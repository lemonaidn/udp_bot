import os
import requests
import json
import csv  # Import the csv module

# Your FEC API key
fec_key = os.environ.get('FEC_API_KEY')

# The URL for the API request
url = f"https://api.open.fec.gov/v1/committee/C00799031/filings/?page=1&per_page=20&cycle=2024&form_type=F24&sort=-receipt_date&sort_hide_null=false&sort_null_only=false&sort_nulls_last=false&api_key={fec_key}"

# Make the GET request
r = requests.get(url, headers={'x-api-key': fec_key})

# Check if the request was successful
if r.status_code == 200:
    # Load the JSON data from the API response
    data = r.json()

    # Define the file path where you want to save the JSON data
    json_file_path = 'api_response.json'

    # Write the JSON data to a file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Data successfully saved to {json_file_path}")

    # Extract the csv_url and pdf_url from each result
    urls = [(result['csv_url'], result['pdf_url']) for result in data['results']]

    # Define the CSV file path where you want to save the URLs
    csv_file_path = 'urls.csv'

    # Write the URLs to a CSV file
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['CSV URL', 'PDF URL'])
        for csv_url, pdf_url in urls:
            writer.writerow([csv_url, pdf_url])

    print(f"URLs successfully saved to {csv_file_path}")
else:
    print("Failed to retrieve data from API")