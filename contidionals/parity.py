def evenOrOdd(n):
    if n % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')


#Another way
def main():
    valueToCheck = int(input('Number to check: '))
    if is_even(valueToCheck):
        print('Even')
    else:
        print('Odd')
        
def is_even(n):
    return n % 2 == 0

# Another way
# return True if n % 2 == 0 else False

main()