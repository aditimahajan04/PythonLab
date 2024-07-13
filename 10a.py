def handle_exceptions_example():
    try:
        # NameError: Trying to access an undefined variable
        print(undefined_variable)
    except NameError as e:
        print(f"NameError occurred: {e}")

    try:
        # IndexError: Trying to access an index that doesn't exist
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError occurred: {e}")

    try:
        # KeyError: Trying to access a key that doesn't exist in a dictionary
        my_dict = {'a': 1, 'b': 2}
        print(my_dict['c'])
    except KeyError as e:
        print(f"KeyError occurred: {e}")

    try:
        # ZeroDivisionError: Trying to divide by zero
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")

def main():
    handle_exceptions_example()

if __name__ == "__main__":
    main()
