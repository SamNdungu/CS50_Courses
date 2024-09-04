# Demonstrates iterating over and index into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
# Print only keys
for stdnt in students:
    print(stdnt)

    
# Print keys and values
for student in students:
    print(student, students[student], sep=", ")
