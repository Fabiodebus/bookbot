from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys


def get_book_text(path_to_book):
    with open(path_to_book, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]

    text = get_book_text(path_to_book)
    

    count_words(text)
    count_characters(text)
    sort_characters(count_characters(text))

    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count --------")
    sorted_chars = sort_characters(count_characters(text))
    for char_dict in sorted_chars:
        print(f"{char_dict['character']}: {char_dict['count']}")

if __name__ == "__main__":
    main()
    