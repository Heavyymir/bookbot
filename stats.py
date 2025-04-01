def get_word_count(book_text):
	 num_words = book_text.split()
	 return len(num_words)

def character_counter(book_text):
	book_text = book_text.lower()
	character_count = {}
	for char in book_text:
		if char in character_count:
			character_count[char] += 1
		else:
			character_count[char] = 1

	return character_count

def sort_on(d):
	return d["num"]

def char_sorted(num_chars_dict):
	sorted_list = []
	for ch in num_chars_dict:
		sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
