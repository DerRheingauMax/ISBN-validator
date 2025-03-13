test = "978-3-8668-0192-9"


def validate_isbn(isbn):
    if not valid_isbn_format(isbn):
        return False
    isbn_number = ""
    prove_number = 0
    for i in isbn:
        if i != "-":
            isbn_number += i
    counter = 0
    for index, i in enumerate(isbn_number):
        if index + 1 == 13:
            break
        if (index + 1) % 2 == 0:
            prove_number += int(i) * 3
        else:
            prove_number += int(i)
        counter += 1
    if 10 - prove_number % 10 == int(isbn_number[-1]):
        return True
    else:
        return False


def valid_isbn_format(isbn):
    dash_indexes = [3, 5, 8, 15]
    if len(isbn) != 17:
        return False
    try:
        for index, i in enumerate(isbn):

            if index in dash_indexes and i != "-":
                return False
            if (index not in dash_indexes) and (type(int(i)) != int):
                return False
    except:
        return False
    return True


if __name__ == "__main__":
    while True:
        isbn = input("isbn: ")
        if isbn == "":
            break
        if not valid_isbn_format(isbn):
            continue
