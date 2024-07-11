import re

def count_occurrences(text):
    # Define the regular expressions for vowels, consonants, and digits
    vowels_pattern = re.compile(r'[aeiouAEIOU]')
    consonants_pattern = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')
    digits_pattern = re.compile(r'\d')

    # Find all occurrences of vowels, consonants, and digits
    vowels = vowels_pattern.findall(text)
    consonants = consonants_pattern.findall(text)
    digits = digits_pattern.findall(text)

    # Count the occurrences
    num_vowels = len(vowels)
    num_consonants = len(consonants)
    num_digits = len(digits)

    return num_vowels, num_consonants, num_digits

def main():
    # Input text
    text = input("Enter the text: ")

    # Count occurrences of vowels, consonants, and digits
    num_vowels, num_consonants, num_digits = count_occurrences(text)

    # Display the counts
    print(f"Number of vowels: {num_vowels}")
    print(f"Number of consonants: {num_consonants}")
    print(f"Number of digits: {num_digits}")

if __name__ == "__main__":
    main()
