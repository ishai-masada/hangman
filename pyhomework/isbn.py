# ISBN Checksum 
#Ishai Masada

def checksum():
    sumDigits = []
    isbn = input("Type in your 10-digit ISBN number: ")
    checksum = int(isbn[-1])
    for idx, digit in enumerate(reversed(isbn)):
        digit = int(digit)
        product = digit*idx
        sumDigits.append(product)
    if (sum(sumDigits)%11) == checksum:
        print("The ISBN number you entered is valid.")
    else:
        print("The ISBN number you entered is not valid.")

checksum()
