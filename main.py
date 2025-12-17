from stats import split_count


def get_book_txt(file_path):
    book = ""
    with open(file_path) as f:
        book = f.read()
    return book


def main():
    file_path = "books/frankenstein.txt"
    book_string = get_book_txt(file_path)
    book_word_count = split_count(book_string)
    print(f"Found {book_word_count} total words")


main()
