# Delete the whitespaces
sttring = '   sttring   '
sttring = sttring.strip()


# Capitalize
name = input('Wich is your name: ')
name = name.capitalize()


print(f'Hello, {name}')

# Separating for variables
first, second = name.split(' ')
print(second)