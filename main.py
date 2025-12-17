from sre_parse import RANGE


def get_book_txt(file_path):
    book = ""
    with open(file_path) as f:
        book = f.read()
        print(book)
    return book


def split_count(book_string):
    book_string = book_string.split()
    for book_string in RANGE(1, 10):
        print(book_string)


def main():
    file_path = "books/frankenstein.txt"
    book_string = get_book_txt(file_path)


main()
