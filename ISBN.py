#user/bin/python
def validate_isbn(isbn):

    """Validate the ISBN format"""

    if len(isbn) != 13:

        return False

    

    try:

        total = 0

        for i in range(0, 12):

            digit = int(isbn[i])

            if i % 2 == 0:

                total += digit

            else:

                total += digit * 3

        check_digit = int(isbn[12])

        calculated_check_digit = (10 - (total % 10)) % 10

        return check_digit == calculated_check_digit

    

    except ValueError:

        return False

def main():

    isbn = input("Please enter your ISBN: ")

    

    if validate_isbn(isbn):

        print("Valid ISBN!")

    else:

        print("Invalid ISBN!")

if __name__ == '__main__':

    main()

