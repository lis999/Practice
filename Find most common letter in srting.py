"""
Find the most common letter in the given string
"""

s = "hello super developer"
char_count = {}

for c in s:
    # if char in char_count:
    #     char_count[char] += 1
    # else:
    #     char_count[char] = 1
    char_count[c] = char_count.setdefault(c, 0) + 1


most_common_char = max(char_count, key=char_count.get)
print(most_common_char)


