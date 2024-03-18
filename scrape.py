import csv
import requests
from bs4 import BeautifulSoup

list_of_rows = []

url = 'https://www.fec.gov/data/filings/?data_type=processed&q_filer=C00799031&cycle=2024&form_type=RFAI&form_type=F5&form_type=F24&form_type=F6&form_type=F9&form_type=F10&form_type=F11'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')

if table:  # Check if the table was found
    for row in table.find_all('tr'):
        list_of_cells = []
        for cell in row.find_all('td'):
            text = cell.text.strip()  # Extract and strip text from each cell
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
else:
    print("No table body found.")

# Writing data to a CSV file
with open('fec_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Filer name', 'Document', 'Version', 'Receipt date', 'Beginning image number'])  # Replace with actual column headers
    writer.writerows(list_of_rows)
