# вывести новые цены на товары в 1ый и 2ой годы зная ставку %

def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)


current_prices = [1.8, 12.65, 56.23, 931.11]
first_percent = int(input('Enter % rate in 1st year: '))
second_percent = int(input('Enter % rate in 2nd year: '))

prices_first = [get_higher_price(first_percent, prices) for prices in current_prices]
second_percent = [get_higher_price(second_percent, prices) for prices in prices_first]

print('Summ of prices in each year: ', round(sum(current_prices), 2), round(sum(prices_first), 2), round(sum(second_percent), 2))