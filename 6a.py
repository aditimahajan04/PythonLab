def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            found = True
            break
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    if found:
        print(f"Key element {key} found at index {mid}.")
    else:
        print(f"Key element {key} not found in the array.")

def main():
    # Example sorted array (can be modified)
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    key = 23  # Define the key element here

    # Perform binary search
    binary_search(sorted_array, key)

if __name__ == "__main__":
    main()
