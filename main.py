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
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {number_of_words} total words
--------- Character Count -------''')
    for char in number_of_characters:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    number_of_words = get_num_of_words(frankenstein)
    number_of_characters = sort_dict_by_value(get_num_of_char(frankenstein))
    print_bookbot(number_of_words, number_of_characters)
    

main()
