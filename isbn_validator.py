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
    elif prove_number % 10 == 0 and int(isbn_number[-1]) == 0:
        return True
    else:
        return False


def valid_isbn_format(isbn):
    if len(isbn) != 17:
        print("wrong format, try with dashes")
        return False
    try:
        dash_count = 0
        for index, i in enumerate(isbn):
            if i == "-" : 
                dash_count +=1
            elif type(int(i)) != int:
                print(f"no int on index: {index}")
                return False
        if dash_count != 4:
            print("more than 4 dashes") 
            return False
    except:
        return False
    return True


if __name__ == "__main__":
    while True:
        isbn = input("isbn: ")
        if isbn == "":
            break
        elif valid_isbn_format(isbn):
            if validate_isbn(isbn):
                print("valid")
            else: 
                print("invalid")
            continue
        else:
            print("wrong formatt")
            continue
