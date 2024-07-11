def find_max_min(array):
    max_num = max(array)
    min_num = min(array)
    return max_num, min_num

def find_second_largest(array):
    max_num = max(array)
    second_largest = float('-inf')
    for num in array:
        if num > second_largest and num < max_num:
            second_largest = num
    return second_largest

def main():
    # Input array
    input_str = input("Enter the numbers in the array separated by spaces: ")
    input_list = input_str.split()
    array = [int(num) for num in input_list]

    # Display the maximum and minimum number from the array
    max_num, min_num = find_max_min(array)
    print(f"Maximum number: {max_num}")
    print(f"Minimum number: {min_num}")

    # Display the second largest number from the array without sorting
    second_largest = find_second_largest(array)
    print(f"Second largest number: {second_largest}")

if __name__ == "__main__":
    main()
