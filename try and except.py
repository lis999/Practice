"""
Given a string s, write a method (function) that will return True if it's a valid single integer or floating number,
or return False if it's not.
"""

s = '   3   '
s1 = ' -5.3    '
s2 = '  3-4'
s3 = '5 8'
s4 = 'zero'

def is_integer_floating(string):
    try:
        float(string) or int(string)
        return True
    except:
        return False

print(is_integer_floating(s4))
