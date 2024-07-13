def create_text_file(filename, max_lines=6):
    lines_entered = 0
    with open(filename, 'w') as file:
        print(f"Enter exactly {max_lines} lines of text:")
        while lines_entered < max_lines:
            line = input()
            file.write(line + '\n')
            lines_entered += 1
            if lines_entered >= max_lines:
                print(f"Maximum {max_lines} lines reached.")
                break
    print(f"File '{filename}' created with {lines_entered} lines.")


def count_characters_in_file(filename):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    uppercase_count += 1
                elif char.islower():
                    lowercase_count += 1
                elif char.isdigit():
                    digit_count += 1

    return uppercase_count, lowercase_count, digit_count


def display_file_details(filename):
    print(f"\nDetails of the file '{filename}':")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


def main():
    filename = "abc.txt"
    create_text_file(filename, max_lines=6)

    uppercase_count, lowercase_count, digit_count = count_characters_in_file(filename)

    display_file_details(filename)

    print(f"Uppercase letters: {uppercase_count}")
    print(f"Lowercase letters: {lowercase_count}")
    print(f"Digits: {digit_count}")


if __name__ == "__main__":
    main()
