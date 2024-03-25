# while True:
#     try:
#         x = int(input('what is x? '))
#     except ValueError:
#         print('x is not an integer')
#     else:
#         break

# print(f"x is {x}")


# # Another way
# while True:
#     try:
#         n = int(input('what is n? '))
#         break
#     except ValueError:
#         print('n is not defined')

# print(f'n is {n}')


### Another way ###
def main():
    x = get_int('what is x? ')
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()


