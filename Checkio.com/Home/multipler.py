def checkio(array: list) -> int:
    d = 0
    if array == []:
        print(0)

    for i in array[0::2]:
        d += i 
    print(d* array[-1])

checkio([])

