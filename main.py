from stats import (
	get_word_count,
	character_counter,
	char_sorted
	)

import sys
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

file_path = sys.argv[1]
print(f"You provided the filepath: {file_path}")


def main():
	book_text = get_book_text(file_path)
	word_count = get_word_count(book_text)
	char_dict = character_counter(book_text) 
	sorted_char = char_sorted(char_dict)
	
	print("============= BOOKBOT =============")
	print(f"Analysing book found at {file_path}")
	print(f"Found {word_count} total words")
	for item in sorted_char:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

def get_book_text(file_path): 
        with open(file_path) as f:
                return f.read()

	

main()
