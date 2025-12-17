def get_book_txt(file_path):
    book = ""
    with open(file_path) as f:
        book = f.read()
        print(book)
    return book


def main():
    file_path = "books/frankenstein.txt"
    book_string = get_book_txt(file_path))


main()
