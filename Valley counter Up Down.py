from itertools import count
# s = 'UUDDUUDDUDUDDDUUDUDUD'
def count_valleys(s):
    valleys = 0
    counter = 0
    is_valley = False
    for i in s:
        if i == 'U':
            counter += 1
        elif i == 'D':
            counter -= 1

        if counter < 0 and not is_valley:    # == False
            is_valley = True

        if counter == 0 and is_valley:
            valleys += 1
            is_valley = False
    return valleys

print(f"Valley passed:{count_valleys('DDUUDDUU')}")

# 2 variant
# s = 'UDDFFUDDUUUFDDDU'
# def counting_valleys(s):
#     level, valleys = 0, 0
#     for step in s:
#         if step == 'U' and level == -1:
#             valleys += 1
#         level += {'U' : 1, 'F' : 0, 'D' : -1}[step]
#     return valleys