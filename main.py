from sre_parse import RANGE

from stats import split_count


def get_book_txt(file_path):
    book = ""
    with open(file_path) as f:
        book = f.read()
    return book


def main():
    file_path = "books/frankenstein.txt"
    book_string = get_book_txt(file_path)
    book_word_list = split_count(book_string)
    return book_word_list


print(f"Found {main()} total words")
