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

# Initialize lists to store the URLs
fec_urls = []
pdf_urls = []

# Extract both the fec_url and pdf_url from each result
# Use get() method to handle cases where 'fec_url' might not be present

for result in data['results']:
    fec_url = result.get('fec_url', 'No FEC URL Found')
    pdf_url = result.get('pdf_url', 'No PDF URL Found')
    fec_urls.append([fec_url])
    pdf_urls.append([pdf_url])

# Define the CSV file paths
fec_csv_file_path = 'fec_urls.csv'
pdf_csv_file_path = 'pdf_urls.csv'

# Write the FEC URLs to a CSV file
with open(fec_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(fec_urls)  # Write each FEC URL

# Write the PDF URLs to a separate CSV file
with open(pdf_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(pdf_urls)  # Write each PDF URL

print(f"FEC URLs successfully saved to {fec_csv_file_path}")
print(f"PDF URLs successfully saved to {pdf_csv_file_path}")