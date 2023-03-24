import re

def remove_numbers(s):
    return re.sub(r'\d', '', s)  # sub заменит цыфры на пустоту в списке

print(remove_numbers('This look5s grea8t!'))