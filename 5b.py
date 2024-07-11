def create_text_file(filename):
    with open(filename, 'w') as file:
        lines = []
        print(f"Enter 5-6 lines of text into '{filename}':")
        for _ in range(5):
            line = input()
            file.write(line + '\n')
            lines.append(line)
        return lines

def find_longest_shortest_words(lines):
    words = []
    for line in lines:
        words.extend(line.split())

    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    return longest_word, shortest_word

def main():
    filename = 'text_file.txt'
    lines = create_text_file(filename)

    longest_word, shortest_word = find_longest_shortest_words(lines)
    print(f"\nLongest word: '{longest_word}', Length: {len(longest_word)}")
    print(f"Shortest word: '{shortest_word}', Length: {len(shortest_word)}")

if __name__ == "__main__":
    main()

#This program will create a new text file named text_file.txt
