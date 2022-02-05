import copy
#####################################################################################
#
# Name:   Ishai Masada
#
# Date:      2/1/22
#
# Purpose:  Use string manipulations
#
# Functions:       is_alphabetical, is_capitalized, is_alphanumeric, lower_to_upper,
#                   upper_to_lower, s_to_j
# Update:           None
#
#####################################################################################

#####################################################################################
#
# Function Name:  is_alphabetical
#
# Date:           2/1/22
#
# Purpose:       Check if the given string is alphabetical by each word
#
# Who called           While loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def is_alphabetical(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    first_letters = []

    for word in sentence:
        first_letters.append(word[0])

    if ''.join(first_letters) in alphabet:
        return "This sentence is alphabetical!"

    else:
        return "This sentence is not alphabetical!"

#####################################################################################
#
# Function Name:  is_capitalized
#
# Date:           2/1/22
#
# Purpose:       Checks if all of the characters in a given string are capitalized
#
# Who called           While loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def is_capitalized(base_string):
    if ''.join(base_string).isupper():
        return "This sentence is capitalized!"

    else:
        return "This sentence is not capitalized!"

#####################################################################################
#
# Function Name:  is_alphanumeric
#
# Date:           2/1/22
#
# Purpose:       Checks if the given string contains numbers and letters
#
# Who called           While Loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def is_alphanumeric(base_string):
    base_string = ''.join(''.join(base_string).split())
    if base_string.isalpha() == False and base_string.isdigit() == False:
        return "This sentence is alphanumeric!"

    else:
        return "This sentence is not alphanumeric!"

#####################################################################################
#
# Function Name:  lower_to_upper
#
# Date:           2/1/22
#
# Purpose:       Capitalizes all of the characters in a given string
#
# Who called           While Loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
##
def lower_to_upper(base_string):
    new_string = copy.deepcopy(base_string)
    for idx, letter in enumerate(new_string):
        if letter == ' ' or letter == '"' or letter.isupper():
            continue
        elif letter.islower():
            new_string[idx] = letter.upper()

    new_string = ''.join(new_string)
    return new_string

#####################################################################################
#
# Function Name:  upper_to_lower
#
# Date:           2/1/22
#
# Purpose:       Converts all of the characters in a given string to lower case
#
# Who called           While Loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def upper_to_lower(base_string):
    new_string = copy.deepcopy(base_string)
    for idx, letter in enumerate(new_string):
        if letter == ' ' or letter == '"' or letter.islower():
            continue
        elif letter.isupper():
            new_string[idx] = letter.lower()

    new_string = ''.join(new_string)
    return new_string

#####################################################################################
#
# Function Name:  s_to_j
#
# Date:           2/1/22
#
# Purpose:       Changes all of the "s"s in a given string to "j"s
#
# Who called           While Loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def s_to_j(base_string):
    new_string = copy.deepcopy(base_string)
    for idx, letter in enumerate(new_string):
        if letter == 's':
            new_string[idx] = 'j'
        if letter == 'S':
            new_string[idx] = 'J'
    return ''.join(new_string)

#####################################################################################
#
# Function Name:  j_to_s
#
# Date:           2/1/22
#
# Purpose:       Changes all of the "j"s in a given string to "s"s
#
# Who called           While Loop
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def j_to_s(base_string):
    new_string = copy.deepcopy(base_string)
    for idx, letter in enumerate(new_string):
        if letter == 'j':
            new_string[idx] = 's'
        if letter == 'J':
            new_string[idx] = 'S'
    return ''.join(new_string)

print("This program is for string manipulation.\n")
for i in range(7):
    base_string = list(input("Type in a sentence here or just hit enter to end the program: "))
    sentence = ''.join(base_string).split()
    if len(''.join(base_string).strip()) == 0:
        break
    print('\n' + is_alphabetical(sentence), '\n')
    print(is_capitalized(sentence), '\n')
    print(is_alphanumeric(base_string), '\n')
    print(lower_to_upper(base_string), '\n')

    # User may want to change the upper case letters to lower case
    print(upper_to_lower(base_string), '\n')

    print(s_to_j(base_string), '\n')

    # User may want to change the "j"s to "s"s
    print(j_to_s(base_string), '\n')
