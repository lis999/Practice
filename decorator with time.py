from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@timeit
def one(num):
    lst = []
    for i in range(num):
        if i % 2 == 0:
            lst.append(i)
    return lst


@timeit
def two(num):
    lst1 = [x for x in range(num) if x % 2 == 0]
    return lst1


l1 = one(10000)
l2 = two(10000)
