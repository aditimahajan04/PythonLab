def main():
    # Input list of strings
    strings = input("Enter a list of strings separated by spaces: ").split()

    # Create list of tuples with string and its length
    tuples_list = [(s, len(s)) for s in strings]

    # Sort the list of tuples by the length of the strings (second element of the tuple)
    sorted_tuples_list = sorted(tuples_list, key=lambda x: x[1])

    # Format the output
    formatted_output = ', '.join([f"{item[0]}:{item[1]}" for item in sorted_tuples_list])

    # Print the formatted output
    print(f"({formatted_output})")

if __name__ == "__main__":
    main()
