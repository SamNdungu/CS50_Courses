# Sorts a list of strings. 
# Print in ascending order

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

