"""
Given a string of space separated numbers, and have to return the highest and lowest number.
high_and_low("1 9 3 4 -5") # return "9 -5"
"""


def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return 'Min:{}, Max:{}'.format(nums[0], nums[-1])


print(high_and_low("1 9 3 4 -5"))


