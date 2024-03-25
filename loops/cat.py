# While Statement
def main():
    ''
    #while_cat()
    #for_cat()
    #nested_loops()
    number = get_number()
    meow(number)

def while_cat():
    counter = 0
    while counter < 3:
        print('meow')
        counter += 1

#Another way
def for_cat():
    # for i in [0,1,2]:
    #     print('meow')
    # Another way
    for _ in range(3):
        print('meow')

#Another way
def nested_loops():
    while True:
        n = int(input('What is n? '))
        if n > 0:
            break
    
    for _ in range(n):
        print('meow')


#Another way with while statement and conditions
def get_number():
    while True:
        n = int(input('What is n? '))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print('meow')

main()

