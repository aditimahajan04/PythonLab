def print_all_items(dictionary):
    print("All items in the dictionary:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def print_all_keys(dictionary):
    print("All keys in the dictionary:")
    for key in dictionary.keys():
        print(key)

def print_all_values(dictionary):
    print("All values in the dictionary:")
    for value in dictionary.values():
        print(value)

def get_password(dictionary, username):
    if username in dictionary:
        print(f"Password for {username}: {dictionary[username]}")
    else:
        print(f"User {username} not found in the dictionary.")

def change_password(dictionary, username, new_password):
    if username in dictionary:
        dictionary[username] = new_password
        print(f"Password for {username} has been changed to: {new_password}")
    else:
        print(f"User {username} not found in the dictionary.")

def main():
    # Initialize the dictionary
    passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}

    # Print all items in the dictionary
    print_all_items(passwd)
    print()

    # Print all keys in the dictionary
    print_all_keys(passwd)
    print()

    # Print all values in the dictionary
    print_all_values(passwd)
    print()

    # Get the password of a user
    get_password(passwd, 'rahul')
    print()

    # Change the password of a particular user
    change_password(passwd, 'ankita', 'brilliant')
    print()

    # Print all items again to see the change
    print_all_items(passwd)

if __name__ == "__main__":
    main()
