# This is the equivalence for a switch on JS
name = input('What´s your name: ')

match name:
    case "Harry" | "Ron" | "Hermione":
        print('Gryffindor')
    case "Draco":
        print('Slytherin')
    case _:
        print('Who?')

