from stats import get_book_text, count_words, count_characters, sort_on, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(path_to_file=sys.argv[1])
    num_words = count_words(file_contents)
    char_count = count_characters(file_contents)
    sorted = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in sorted:
        if items["char"].isalpha():
            print(f"{items["char"]}: {items["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
