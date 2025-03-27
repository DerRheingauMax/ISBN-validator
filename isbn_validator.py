def validate_isbn(isbn):
    valid_format, error = valid_isbn_format(isbn)
    if not valid_format:
        return False, error
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
        return True, ""
    elif prove_number % 10 == 0 and int(isbn_number[-1]) == 0:
        return True, ""
    else:
        return False, ""


def valid_isbn_format(isbn):
    if len(isbn) != 17:
        return False, "falsches Format"
    try:
        dash_count = 0
        for index, i in enumerate(isbn):
            if i == "-" : 
                dash_count +=1
            elif type(int(i)) != int:
                return False, f"keine Zahl an Stelle: {index+1}"
        if dash_count != 4:
            return False, "mehr als 4 Striche"
    except:
        return False, "unknown"
    return True, ""


if __name__ == "__main__":
    while True:
        isbn = input("isbn: ")
        if isbn == "":
            break
        elif valid_isbn_format(isbn)[0]:
            valid, error = validate_isbn(isbn)
            if valid:
                print("valid")
            else: 
                print(f'invalid: {error}')
            continue
        else:
            print(f'wrong format: {valid_isbn_format(isbn)[1]}')
            continue
