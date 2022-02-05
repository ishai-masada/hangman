# bin Function

def zero_one(number):
    binary_number = []
    power = 0
    while number - 2**(power) > 0:
        power += 1
    for place_holder in range(power):
        if place_holder == 1:
            place_holder = power+1
        if place_holder == 0:
            place_holder = power+2
        binary_number.append(str(place_holder))
    binary_number = list(reversed(binary_number))
    exponents = [int(num) for num in binary_number]
    exponents.remove(exponents[-1])
    exponents.remove(exponents[-1])
    exponents.append(1)
    exponents.append(0)
    zipped_list = zip(binary_number, exponents)
    for digit, exp in zipped_list:
        if number - 2**exp < 0:
            binary_number.insert(binary_number.index(digit), '0')
            binary_number.remove(digit)
            continue
        elif number - 2**exp >= 0:
            number -= 2**exp
            binary_number.insert(binary_number.index(digit), '1')
            binary_number.remove(digit)
    result = '0b' + ''.join(binary_number)
    print(result)

zero_one(int(input('Type in a number: ')))
