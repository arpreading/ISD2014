s = "((1-2+3)*5+10/2)+4.5"


def split_operators(s):
    numbers = "0123456789."
    operators = []
    integers = []
    last_number = ""
    for value in s:
        if value in numbers:
            last_number += value
        else:
            if last_number:
                integers.append(last_number)
                last_number = ""
            if value:
                operators.append(value)
    if last_number:
        integers.append(last_number)
    return operators + integers

print (split_operators(s))
