# Sorts a list of dictionaries using a function

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({'name': name, 'house': house})

def get_name(student):
    return student['name']

def get_house(student):
    return student['house']

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

print()

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")