
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    num_words = 0
    text = text.split()
    for words in text:
        num_words += 1
    return num_words


def count_characters(text):

    letter_counts = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
            '.': 0,
            '!': 0,
            '?': 0,
            ',': 0,
            ' ': 0
    }


    for char in text:
        char = char.lower()
        if char in letter_counts:
            letter_counts[char] += 1

    return letter_counts

def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    list_of_dicts = []
    for k, v in dictionary.items():
        new_dict = {"char": k, "num": v}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
