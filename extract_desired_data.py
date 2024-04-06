import os
import csv
import fecfile

# Define the directory where .fec files are stored
directory_path = 'fec_files'

# Define the CSV file path for storing the results, appending the timestamp
csv_file_base = 'last_twenty_ind_expenditures_df'
csv_file_extension = '.csv'
csv_file_path = f'{csv_file_base}{csv_file_extension}'

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

# Assuming all_data has been filled with all records from .fec files as before

# New file path for storing new records
new_records_file_path = 'new_records.csv'

# Read existing filenames from last_twenty_ind_expenditures_df.csv
existing_filenames = set()
try:
    with open(csv_file_path, mode='r', encoding='utf-8') as existing_csv:
        reader = csv.reader(existing_csv)
        next(reader, None)  # Skip the header row
        for row in reader:
            existing_filenames.add(row[0])  # Assuming 'Filename' is the first column
except FileNotFoundError:
    print(f"No existing file found at {csv_file_path}. All data will be considered new.")

# Compare and identify new records based on filenames
new_records = [row for row in all_data if row[0] not in existing_filenames]

# Write new records to new_records.csv, if any
with open(new_records_file_path, mode='w', newline='', encoding='utf-8') as new_csv:
    writer = csv.writer(new_csv)
    writer.writerow(['Filename', 'Amount', 'Candidate Name', 'Support/Oppose', 'District', 'State', 'Purpose', 'YTD Amount', 'Election'])  # Always write header
    
    if new_records:
        writer.writerows(new_records)
        print(f"New records extracted to CSV file: {new_records_file_path}")

        # Overwrite last_twenty_ind_expenditures_df.csv with all records since new ones were found
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as all_csv:
            all_writer = csv.writer(all_csv)
            all_writer.writerow(['Filename', 'Amount', 'Candidate Name', 'Support/Oppose', 'District', 'State', 'Purpose', 'YTD Amount', 'Election'])  # Write header
            all_writer.writerows(all_data)
        print(f"All records have been written to {csv_file_path}.")
    else:
        print("No new records found. An empty new_records.csv file has been created.")