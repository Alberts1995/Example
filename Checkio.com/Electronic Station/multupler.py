def checkio(number: int) -> int:
    d = 1
    for x in str(number):
        if int(x) > 0:
            d *= int(x)
    print(d)

checkio(123405)




