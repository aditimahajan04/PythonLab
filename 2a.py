def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Input range
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    # List to store prime numbers
    prime_numbers = []

    # Find and collect all prime numbers in the given range
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)

    # Display prime numbers
    print("Prime numbers in the given range:")
    print(prime_numbers)

if __name__ == "__main__":
    main()
