def get_book_text(path):
    with open(path) as f:   # Opening a file and storing it in f
        return f.read()     # Returning the entire file as a string

def get_num_of_words(words):
    list = words.split()
    return len(list)

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    number_of_words = get_num_of_words(frankenstein)
    print(f"{number_of_words} words found in the document")

main()
