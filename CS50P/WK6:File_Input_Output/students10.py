# Writes a CSV file using csv.writer
import csv

name = input("What is Your Name? ")
home = input("What is Your Home? ")


# Write in files using `csv.writer`
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])