def main():
    # Create a list with all the subject names of the 4th semester
    subjects = [
        "Data Analysis and Algorithms",
        "Maths",
        "Data Communication and Networking",
        "Finite Automata and Formal Languages",
        "Python Programming Lab",
        "Data Analysis using R",
    ]

    # Display the list using a for loop
    print("List of subjects:")
    for subject in subjects:
        print(subject)

    # Display 2nd and 5th element of the list
    print("\n2nd element:", subjects[1])
    print("5th element:", subjects[4])

    # Display first 4 elements of the list using the range of indexes
    print("\nFirst 4 elements:", subjects[:4])

    # Display last 4 elements of the list using the range of negative indexes
    print("\nLast 4 elements:", subjects[-4:])

    # Display if "Python Programming Lab" is available in the list or not
    if "Python Programming Lab" in subjects:
        print("\n'Python Programming Lab' is available in the list.")
    else:
        print("\n'Python Programming Lab' is not available in the list.")

    # Demonstrate the working of append() function
    subjects.append("Microcontrollers and IOT")
    print("\nList after appending 'Artificial Intelligence':", subjects)

    # Demonstrate the working of insert() function
    subjects.insert(3, "Data Analysis and Algorithm Lab")
    print("\nList after inserting 'Machine Learning' at index 3:", subjects)

    # Demonstrate the working of remove() function
    subjects.remove("Maths")
    print("\nList after removing 'Maths':", subjects)

    # Demonstrate the working of pop() function
    popped_subject = subjects.pop()
    print("\nList after popping the last element:", subjects)
    print("Popped element:", popped_subject)


if __name__ == "__main__":
    main()
