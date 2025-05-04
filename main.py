from stats import *
import sys

def main():

    bookargs = sys.argv

    if len(bookargs) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = bookargs[1]
    text = get_book_text(book_path)
    
    print("--- Begin report of books/frankenstein.txt ---")

    wc = count_words(text)
    print(f"{wc} words found in the document\n")

    cc = count_characters(text)
    print_chars(cc)

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()