import math
import os

def user_friendly_size(file_size) -> str:
    symbols = ('B', 'kB', 'MB', 'GB', 'TB')
    if isinstance(file_size, str):      # Если аргумент - строка
        if file_size.isdigit():         # Если протупили и отправили число строкой
            file_size = int(file_size)
        else:
            file_size = os.stat(file_size).st_size   # получим размкр файла в байтах
    sym_index = int(math.log(file_size, 2) // 10)
    return f'{file_size / 2 ** (sym_index * 10) :.2f} {symbols[sym_index]}'
