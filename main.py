def get_book_text(path):
    with open(path) as f:   # Opening a file and storing it in f
        return f.read()     # Returning the entire file as a string

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(frankenstein)

main()
