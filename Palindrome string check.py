# function which return reverse of a string

def is_palindrome(s):
    return s == s[::-1]
#driver code
s = input('Enter your word: ')
answer = is_palindrome(s)

if answer:
    print('Yes')
else:
    print('No')