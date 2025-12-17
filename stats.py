def split_count(book_string):
    book_list = book_string.split()
    book_count = len(book_list)
    return book_count


def letter_count(book_string):
    letter_dictionary = {}
    book_string = book_string.lower()
    letter_list = list(book_string)
    for l in letter_list:
        if l not in letter_dictionary:
            letter_dictionary[l] = 1
        elif l in letter_dictionary:
            letter_dictionary[l] += 1
        else:
            print("somthings went weird here")
    return letter_dictionary
