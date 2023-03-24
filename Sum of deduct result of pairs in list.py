"""Your task is to sum the difference  between consecutive pair in the array in descending order.
Example: [2, 1, 10] -> 9
In descending order: [10, 2, 1]
Sum: max - min = 8-1 = 9
If the array is empty or array has only one element the result should be 0
"""
given_array = [9, 1, 4, 13, 90]

def sum_of_diff(arr):
    if len(arr) <= 1:
        return 0

    diff = []
    arr.sort(reverse = True)
    for i in range(len(arr)):
        if i + 1 < len(arr):
            t = abs(arr[i] - arr[i + 1])
            diff.append(t)
    return sum(diff)
print(sum_of_diff(given_array))


# в данном решении не надо сортировать список, а просто использовать "min & max"
def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0
print(sum_of_differences(given_array))



