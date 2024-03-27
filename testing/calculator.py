def main():
    x = int(input('What´s x? '))
    result = square(x)
    print(f'x squared is {result}')


def square(n):
    return n * n

if __name__ == "__main__":
    main()

