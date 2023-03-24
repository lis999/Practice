"""
In order to find out what the word is, you should use an array of 3 numbers to retrieve 3 letters
from the comment (string) that create the word.
Each of the numbers in the array refers to the position of a letter in the string, in increasing order.
Spaces are not places, you need the actual letters. No spaces.
The returned word should be all lowercase letters.
if you can't find one of the letters using the index numbers, return "No mission today". Jenny would be very sad, but that's life... :(
Example: input: [5, 0, 3], "I Love You" output: "ivy" (0 = "i", 3 = "v", 5 = "y")
"""

def missing(nums, s):
    s = s.replace(' ', '').lower()
    s1 = ''
    for i in range(len(s)):
        if i in nums:
            s1 += s[i]
    if len(s1) < 3:
        return 'No mission today'
    return s1


print(missing([5, 0, 3], "I Love You"))
