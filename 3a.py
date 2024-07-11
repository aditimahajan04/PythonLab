def add_entry(dictionary):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    dictionary[word] = meaning
    print(f"Entry added: {word} - {meaning}")

def search_word(dictionary):
    word = input("Enter the word to search: ")
    if word in dictionary:
        print(f"Meaning of '{word}': {dictionary[word]}")
    else:
        print(f"'{word}' not found in the dictionary.")

def find_words_with_meaning(dictionary):
    meaning = input("Enter the meaning to search: ")
    words = [word for word, word_meaning in dictionary.items() if word_meaning == meaning]
    if words:
        print(f"Words with meaning '{meaning}': {', '.join(words)}")
    else:
        print(f"No words found with meaning '{meaning}'.")

def remove_entry(dictionary):
    word = input("Enter the word to remove: ")
    if word in dictionary:
        del dictionary[word]
        print(f"Entry '{word}' removed.")
    else:
        print(f"'{word}' not found in the dictionary.")

def display_sorted_words(dictionary):
    sorted_words = sorted(dictionary.keys())
    print("Words sorted alphabetically:")
    for word in sorted_words:
        print(word)

def main():
    dictionary = {}
    while True:
        print("\nDictionary Menu:")
        print("1. Add a new entry")
        print("2. Search for a word")
        print("3. Find words with the same meaning")
        print("4. Remove an entry")
        print("5. Display all words sorted alphabetically")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_entry(dictionary)
        elif choice == 2:
            search_word(dictionary)
        elif choice == 3:
            find_words_with_meaning(dictionary)
        elif choice == 4:
            remove_entry(dictionary)
        elif choice == 5:
            display_sorted_words(dictionary)
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
