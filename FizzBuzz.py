"""
print the number from 1 to 10
if the value is multiple of 3 => Fizz
if the value is multiple of 5 => Buzz
if the value is multiple of 3 and 5 => FizzBuzz
others => number
"""
number = int(input('Enter your number: '))
for num in range(1, number + 1):
    if (num % 3 == 0) and (num % 5 == 0):
        print(num, ' - FizzBuzz')
    elif num % 3 == 0:
        print(num, ' - Fizz')
    elif num % 5 == 0:
        print(num, ' - Buzz')
    else:
        print(num, ' - ')