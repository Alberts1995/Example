def replace_first(items: list):
    items[-1], items[0] = items[0], items[-1]
    print(items) 

replace_first([1, 2, 3, 4, 5])



