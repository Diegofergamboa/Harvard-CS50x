def main():
    ''
    #student_printer()
    #dict_printer()


def student_printer():
    students = ['Hermione', 'Harry', 'Ron']
    
    #### Another way #####
    # for i in range(len(students)):
    #     print(students[i])
    
    #### Another way #####
    # for student in students:
    #     print(student)

    #### Another way #####
    for i in range(len(students)):
        print(i, students[i])


def dict_printer():
    # Old way to represent information wth lists
    students = ['Hermione', 'Harry', 'Ron', 'Draco']
    houses = ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Slytherin']

    # Dic Syntax {} with curly brackets
    dict_students = {
        'Hermione' : 'Gryffindor',
        'Ron' : 'Gryffindor',
        'Harry' : 'Gryffindor',
        'Draco' : 'Slytherin'
    }

    # Printing Doctionaries
    print(dict_students['Hermione'])
    
    #### Another way ####
    for student in dict_students:
        print(student)

    #### Another way ####
    for student in dict_students:
        print(student, dict_students[student])


def multi_directories():
    #### Dictionaries based on list and Dictionaries  ####
    multi_students = [
        {
            'name': 'Hermione',
            'house': 'Gryffindor',
            'patronus': 'Otter'
        },
                {
            'name': 'Harry',
            'house': 'Gryffindor',
            'patronus': 'Stag'
        },
                {
            'name': 'Ron',
            'house': 'Gryffindor',
            'patronus': 'Jack Rusell terrier'
        },
                {
            'name': 'Draco',
            'house': 'Slytherin',
            'patronus': None
        },
    ]

main()