import csv

# Path to the CSV files
updated_csv_path = 'csv_output.csv'  # Replace with your CSV file path

# Path to the new CSV file
new_csv_path = 'desired_data.csv'  # Replace with your desired output file path

# The indices of the columns we want to include, zero-based
included_column_indices = [17, 19, 20, 22, 23, 26, 28, 29, 33, 34, 35]

# Read the original CSV and write the filtered data to the new CSV
with open(updated_csv_path, 'r') as infile, open(new_csv_path, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the headers for the included columns
    # We are using the included_column_indices to extract the headers
    headers = next(reader)
    writer.writerow([headers[index] for index in included_column_indices])

    # Write the data rows
    for row in reader:
        filtered_row = [row[index] for index in included_column_indices]
        writer.writerow(filtered_row)

# The new CSV file is now created at the 'new_csv_path'.