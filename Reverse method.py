a = 'mamba'

def solution(a):
    temp = list(a)
    temp.reverse()
    return ''.join(temp)

print(solution(a))



# solution #2

# solution_2 = str(lambda a: a[::-1])
# print(solution_2)