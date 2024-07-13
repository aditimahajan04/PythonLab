def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operand type(s) for division!")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
    else:
        print(f"The result of {a} / {b} is {result}")
    finally:
        print("Division operation complete.")

def main():
    # Example 1: Handling division by zero
    divide_numbers(10, 0)

    # Example 2: Handling unsupported operand type
    divide_numbers(10, '2')

    # Example 3: Handling valid division
    divide_numbers(10, 2)

if __name__ == "__main__":
    main()
