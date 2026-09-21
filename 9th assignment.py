import csv
import json

with open("input.csv", "r", newline="") as csv_data:
    reader = csv.DictReader(csv_data)
    records = list(reader)

with open("output.json", "w") as json_data:
    json.dump(records, json_data, indent=4)

print("CSV data successfully converted to JSON.")
print("Output stored in output.json")