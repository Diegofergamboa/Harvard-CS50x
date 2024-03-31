### A way to save and iterate CSV data ###
# with open("./files_io/students.csv") as file:
#     for line in file:
#         row = line.strip().split(",")
#         print(f"{row[0]} is in the house of {row[1]}")


### A way to save and iterate CSV data with lists ###
# students = []

# with open("./files_io/students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)



### A way to save and iterate CSV data with a dictionary ###
students = []

with open("./files_io/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # Saving information as keys and values for the dic
        student = {"name" : name, "house" : house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
