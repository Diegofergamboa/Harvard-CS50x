from calculator import square

def main():
    test_square()

def test_square():
    ### Classic way to use the testing functions ###
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")
    # if square(7) != 49:
    #     print("7 squared was not 49")

    ### Another way ###
    # assert square(2) == 4
    # assert square(3) == 9
    # assert square(7) == 49


    ### Another way ###
    try:
        assert square(3) == 9
    except AssertionError:
        print('3 squares was not 9')
    try:
        assert square(-7) == 49
    except AssertionError:
        print('-7 squares was not 49')
    try:
        assert square(-2) == 4
    except AssertionError:
        print('-2 squares was not 4')

if __name__ == "__main__":
    main()