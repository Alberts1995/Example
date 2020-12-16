import math

def split_list(items: list) -> list:
    w = []
    if len(items) % 2 == 0:
        x = len(items)//2
        w.append(items[0:x])
        w.append(items[x:])
    else:
        y = (len(items) / 2)
        z = math.ceil(y)
        w.append(items[0:z])
        w.append(items[z:])
    print(w)

split_list([1, 2, 3])
