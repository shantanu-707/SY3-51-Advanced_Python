import json
import csv

with open("students.json", "r") as f:
    students = json.load(f)

with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

print("Converted", len(students), "records to students.csv")
