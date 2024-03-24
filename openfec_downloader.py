import os
import json
import requests


fec_key = os.environ.get('FEC_API_KEY')

url = f"https://api.open.fec.gov/v1/committee/C00799031/filings/?page=1&per_page=20&cycle=2024&form_type=F24&sort=-receipt_date&sort_hide_null=false&sort_null_only=false&sort_nulls_last=false&api_key={fec_key}"

r = requests.get(url, headers={'x-api-key': fec_key})

# Print the response from the API (for debugging purposes)
print(r.json())