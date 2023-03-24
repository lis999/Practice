n_num = int(input('How many fibonacci numbers? '))
f0 = 0 # start point
f1 = 1 # next step for calculation

for count in range(n_num):
    fib = f0 + f1
    f0 = f1 # идет подмена знчение для дальнейшего расчета
    f1 = fib
    print(f'{fib}')