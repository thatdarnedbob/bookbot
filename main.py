from stats import *

def main():
    book_path = "books/frankenstein.txt"
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