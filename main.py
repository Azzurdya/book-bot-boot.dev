from stats import letter_count, split_count


def get_book_txt(file_path):
    book = ""
    with open(file_path) as f:
        book = f.read()
    return book


def sort_format(letter_dictionary):
    for i in letter_dictionary:
        print(f"{i}: {letter_dictionary[i]}")


def main():
    file_path = "books/frankenstein.txt"
    book_string = get_book_txt(file_path)
    book_word_count = split_count(book_string)
    letter_dictionary = letter_count(book_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    sort_format(letter_dictionary)


main()
