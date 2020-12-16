def replace_first(items: list):
    for num in items:
        items.append(num)
        del items[0]
        break
    print(items)

replace_first([1])



