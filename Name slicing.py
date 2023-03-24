# def who_is_paying(name):
#     if len(name) <= 2:
#         return list(name)
#     else:
#         return list(name, name[0:2])
#
#


def who_is_paying(name):
    return [name, name[0:2]] if len(name) > 2 else [name]


print(who_is_paying('Julia'))