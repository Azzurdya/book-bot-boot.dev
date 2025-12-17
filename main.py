from sre_parse import RANGE


def get_book_txt(file_path):
    book = ""
    with open(file_path) as f:
        book = f.read()
        print(book)
    return book


def split_count(book_string):
    book_string = book_string.split()
    book_count = len(book_string)
    return book_count


def main():
    file_path = "books/frankenstein.txt"
    book_string = get_book_txt(file_path)
    book_word_list = split_count(book_string)
    return book_word_list


print(main())
