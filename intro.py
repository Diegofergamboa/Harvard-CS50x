#! Potetial function to check the type of variable
def checkTypeOf(entry):
    return type(entry)


name = 123
print(checkTypeOf(name))


# This is another way to check the concat of the var and string
print(f'this is the var "{name}", of the variables and the type is {checkTypeOf(name)}')

