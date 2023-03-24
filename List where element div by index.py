# Return a new array consisting of elements which are multiple of their own index in input array (length >1).
# example: [22, -6, 32, 82, 9, 25] ->  [-6, 32, 25]

lst = [22, -6, 32, 82, 9, 25]
new_lst = []

for i, el in enumerate(lst[1:], start = 1):
    if el % i == 0:
        new_lst.append(el)
print(new_lst)