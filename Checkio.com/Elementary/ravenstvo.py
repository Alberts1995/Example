from typing import List, Any


def all_the_same(elements) -> bool:
    if elements[1:] == elements[:-1]:
        return print(True)
    else:
        return print(False)


a = input().split(' ')
all_the_same(a)