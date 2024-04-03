import os
import csv
import fecfile
from datetime import datetime

# Define the directory where .fec files are stored
directory_path = 'fec_files'

# Generate a timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Define the CSV file path for storing the results, appending the timestamp
csv_file_base = 'last_twenty_ind_expenditures_df'
csv_file_extension = '.csv'
csv_file_path = f'{csv_file_base}_{timestamp}{csv_file_extension}'

# Prepare to collect data from all .fec files
all_data = []

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.fec'):
        file_path = os.path.join(directory_path, filename)
        
        # Open and parse the .fec file
        with open(file_path, 'r') as file:
            data = fecfile.loads(file.read())
            
            # Extract information from 'Schedule E' itemizations
            for item in data.get('itemizations', {}).get('Schedule E', []):
                # Extract relevant fields
                amount = item.get('expenditure_amount')
                candidate_name = f"{item.get('candidate_first_name', '')} {item.get('candidate_last_name', '')}".strip()
                support_oppose = 'Support' if item.get('support_oppose_code') == 'S' else 'Oppose'
                district = item.get('candidate_district')
                state = item.get('candidate_state')
                purpose = item.get('expenditure_purpose_descrip')
                ytd_amount = item.get('calendar_y_t_d_per_election_office')
                election = 'Primary' if item.get('election_code') == 'P2024' else 'General'
                
                # Add the extracted information to the all_data list along with the filename
                all_data.append([filename, amount, candidate_name, support_oppose, district, state, purpose, ytd_amount, election])

# Write the collected data to a CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Add 'Filename' to the header row
    writer.writerow(['Filename', 'Amount', 'Candidate Name', 'Support/Oppose', 'District', 'State', 'Purpose', 'YTD Amount', 'Election'])
    writer.writerows(all_data)

print(f"Data extracted to CSV file: {csv_file_path}")
