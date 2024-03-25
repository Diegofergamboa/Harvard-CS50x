def main():
    print_squeare(3)


def print_squeare(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print('#', end='')
        print()

main()