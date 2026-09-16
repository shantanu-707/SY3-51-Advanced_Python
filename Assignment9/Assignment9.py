import csv
import json

input_file = "input.csv"
output_file = "output.json"

data = []

# Read data from CSV file
with open(input_file, "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        data.append(dict(row))


# Write data into JSON file
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)


print("CSV file converted to JSON successfully.")