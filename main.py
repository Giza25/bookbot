from stats import get_num_of_words
from stats import get_num_of_char
from stats import sort_dict_by_value
import sys

def get_book_text(path):
    with open(path) as f:   # Opening a file and storing it in f
        return f.read()     # Returning the entire file as a string
    
def print_bookbot(number_of_words, number_of_characters):
    print(f'''
============ BOOKBOT ============
Analyzing book found at books/book.txt...
----------- Word Count ----------
Found {number_of_words} total words
--------- Character Count -------''')
    for char in number_of_characters:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def check_arguments(argv):
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_arguments(sys.argv)

    # Handling different cases of incorrect usage
    try:
        book = get_book_text(sys.argv[1])
    except IsADirectoryError:
        print("You cannot use a directory!")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found or doesn't exist!")
        sys.exit(1)
    
    number_of_words = get_num_of_words(book)
    number_of_characters = sort_dict_by_value(get_num_of_char(book))
    print_bookbot(number_of_words, number_of_characters)
    

main()
