def remove_all_before(items: list, border: int):
    x = -1
    for num in items:
        x +=1
        if num == border:
            print(items[x:])
            break

    print(items)

remove_all_before([1, 2, 2, 4, 5], 3) 



        

