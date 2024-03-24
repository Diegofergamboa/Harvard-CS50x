def main():
    x = int(input('what is x: '))
    print('x squared is ', square(x))

# Pow function to check for squares
def square(n):
    return pow(n, 2)

main()