def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose the operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        print("Result: ", add(num1, num2))
    elif choice == 2:
        print("Result: ", subtract(num1, num2))
    elif choice == 3:
        print("Result: ", multiply(num1, num2))
    elif choice == 4:
        print("Result: ", divide(num1, num2))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
