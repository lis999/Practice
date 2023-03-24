def sum_factorials(num):
    part_factorial = 1
    summa = 0

    for i in range(1, n + 1):
        part_factorial *= i
        summa += part_factorial
    return summa

n = int(input('Enter your number: '))
print(sum_factorials(n))
