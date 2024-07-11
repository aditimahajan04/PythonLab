def add_items(tup, items):
    return tup + tuple(items)

def display_length(tup):
    print(f"Length of the tuple: {len(tup)}")

def check_item(tup, item):
    if item in tup:
        print(f"Item '{item}' is in the tuple.")
    else:
        print(f"Item '{item}' is not in the tuple.")

def access_item(tup, index):
    if 0 <= index < len(tup):
        print(f"Item at index {index}: {tup[index]}")
    else:
        print("Index out of range.")

def main():
    # Create a tuple
    tup = ('apple', 'banana', 'cherry')

    # Display the initial tuple
    print("Initial tuple:", tup)

    # Add items to the tuple
    new_items = ['date', 'elderberry']
    tup = add_items(tup, new_items)
    print("Tuple after adding items:", tup)

    # Display the length of the tuple
    display_length(tup)

    # Check for an item in the tuple
    check_item(tup, 'banana')
    check_item(tup, 'fig')

    # Access an item in the tuple
    access_item(tup, 1)
    access_item(tup, 5)

if __name__ == "__main__":
    main()
