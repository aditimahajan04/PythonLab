import random

def generate_random_numbers(count, start=1, end=10000):
    return [random.randint(start, end) for _ in range(count)]

def is_odd(number):
    return number % 2 != 0

def is_length_valid(number, valid_lengths):
    return len(str(number)) in valid_lengths

def display_odd_numbers_with_valid_length(numbers, valid_lengths):
    print("Odd numbers with valid lengths:")
    for number in numbers:
        if is_odd(number) and is_length_valid(number, valid_lengths):
            print(number)

# Generate 20 random numbers
random_numbers = generate_random_numbers(20, 1, 9999)
print("Generated random numbers:", random_numbers)

# Define valid lengths
valid_lengths = {2, 4}

# Display odd numbers with valid lengths
display_odd_numbers_with_valid_length(random_numbers, valid_lengths)
