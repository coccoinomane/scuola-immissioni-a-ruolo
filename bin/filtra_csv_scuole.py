# Read the CSV passed to the script as argument and print only the
# rows where the given column is equal to the given value

import csv
from sys import argv
from typing import Any, List

usage = "Usage: python3 -m bin.filtra_csv_scuole <file CSV con le scuole> <colonna> <valore> <file CSV di destinazione>"

# When called with no arguments, print help message
if len(argv) == 1:
    print(usage)
    exit(0)

# Make sure the CSV file exists
try:
    csv_file = argv[1]
    open(csv_file)
except FileNotFoundError:
    print(f"File {csv_file} not found")
    exit(1)

# Makse sure the column is specified
try:
    column = argv[2]
except IndexError:
    print(usage)
    exit(1)

# Makse sure the value is specified
try:
    value = argv[3]
except IndexError:
    print(usage)
    exit(1)

# Make sure the output CSV file is specified
try:
    output_csv_file = argv[4]
except IndexError:
    print(usage)
    exit(1)

# Extract headers from the CSV file
with open(csv_file, newline="") as f:
    headers = list(csv.reader(f))[0]
    
# Read in memory the CSV file
with open(csv_file, newline="") as f:
    csv_array = list(csv.reader(f))

# Print the number of rows before applying the filter
print(f"Number of rows: {len(csv_array)}")
print("")

# Find the index of the column DESCRIZIONECOMUNE
# in the first CSV array
try:
    index = [h.lower() for h in headers].index(column.lower())
except ValueError:
    print(f"Column {column} not found")
    exit(1)
print(f"Index of {headers[index]}: {index}")
print("")

# Save to a separate array the CSV rows that match the filter
csv_array_filtered: List[List[Any]] = []
for row in csv_array:
    if row[index].lower() == value.lower():
        csv_array_filtered.append(row)

# Print the number of rows after applying the filter
print(f"Number of rows after filtering: {len(csv_array_filtered)}")
print("")

# Save output CSV file, including headers
with open(output_csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(csv_array_filtered)
