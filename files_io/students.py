import csv

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



# ### A way to save and iterate CSV data with a dictionary ###
# students = []

# with open("./files_io/students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # Saving information as keys and values for the dic
#         student = {"name" : name, "house" : house}
#         students.append(student)


# # Functions to pass as parameters
# def get_name(student):
#     return student['name']

# def get_house(student):
#     return student['house']

# # Passing functions as parameters into functions
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")



# # ### A way to save and iterate using lambda

# students = []

# with open("./files_io/students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name , "house" : house}
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")


# ### A way to save and iterate using CSV and lambda

# students = []

# with open("./files_io/students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")



# # ### A way to save and iterate using CSV Dict Reader and lambda
# students = []

# with open("./files_io/students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

### A way to save and iterate using CSV Dict Reader and lambda
name = input('what is your name? ')
home = input('what is your home? ')

with open("./files_io/students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name" , "home"])
    writer.writerow({"name" : name, "home": home})