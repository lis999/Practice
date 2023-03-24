# 4521369741 → you have to find the sum of these numbers until it’s a single-digit number
from functools import reduce

def reduce_number_1(number):
    convert_number = [i for i in str(number)]
    while len(convert_number) > 1:
        count = 0
        for i in convert_number:
            count += int(i)
        convert_number = [i for i in str(count)]
    return count



def reduce_number_2(number):
    while len(str(number)) > 1:
        number = sum(map(int, str(number)))
    return number





def reduce_number_3(number):
    while len(str(number)) > 1:
        number = reduce(lambda a, b: a + b, map(int, str(number)))
    return number

print(reduce_number_1(4521369741))