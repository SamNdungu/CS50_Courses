# Writes a CSV file using csv.DictWriter

import csv 

name = input("What's Your Name? ")
home = input("What's Your Home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})