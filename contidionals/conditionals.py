x = int(input('First number: '))
y = int(input('Second number: '))


if x < y:
    print(f'{x} is greater than {y}')
elif x > y:
    print(f'{y} is greater than {x}')
else:
    print(f'{x} and {y} are equals')


# Another way
if x == y:
    print('Values are equal')
else:
    print('Values are not equal')



# Another way
if x != y:    
    print('Values are not equal')
else:
    print('Values are equal')


