"""
Given a mixed array of number and string representations of integers, add up the non-string integers
and subtract the total of the string integers.
Return as a number.
"""


def div_con(lst):
    return sum(x if isinstance(x, int) else -int(x) for x in lst)


new_lst = [5, '11', -9, 100, '-28', '96']
print(div_con(new_lst))
