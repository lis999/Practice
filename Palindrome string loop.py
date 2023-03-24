# Python program to check if a string is palindrome or not

# word = input('Enter your word: ')
# new_word = ""
# for letter in word:
#     new_word = letter + new_word
# if (word == new_word):
#     print("Yes")
# else:
#     print("No")

# Using list method
word = input('Enter your word: ')
rev_word = list(word[::-1])
print(rev_word)
new_word = ''
for letter in rev_word:
    new_word += letter
if new_word == word:
    print('Word - ', word, 'is palindrome')
else:
    print('Word - ', word, 'is not palindrome')