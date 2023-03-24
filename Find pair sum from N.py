input_number = int(input('Enter your number: ')) #4
input_array = [1, 43, 6, 3, 2]
result = []

for number in input_array:
    second_number = input_number - number
    if second_number in input_array and second_number != number:
        result.append((number, second_number))
print(list(set(result)))
