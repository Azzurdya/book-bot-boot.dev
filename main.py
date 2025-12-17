import sys

from stats import letter_count, split_count

len_sys = 0


def get_book_txt(file_path):
    book = ""
    with open(file_path) as f:
        book = f.read()
    return book


def sort_format(letter_dictionary):
    for i in letter_dictionary:
        print(f"{i}: {letter_dictionary[i]}")


def main(file_path):
    book_string = get_book_txt(file_path)
    book_word_count = split_count(book_string)
    letter_dictionary = letter_count(book_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    sort_format(letter_dictionary)


print(sys.argv)

len_sys = len(sys.argv)

if len_sys != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif len_sys == 2:
    main(sys.argv[1])
