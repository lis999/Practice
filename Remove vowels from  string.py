""" Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel."""

def disemvowel(string_):
    return ''.join(x for x in string_ if x not in 'AEOUIaeoui')


def disemvowel1(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s


print(disemvowel("This website is for losers LOL!"))
print(disemvowel1("This website is for losers LOL!"))