def checkio(numbers_array):
    number = []
    number_new = []
    for x in numbers_array:
        number.append(abs(x))
    for z in sorted(number):
        for y in numbers_array:
            if z * -1 == y:
                number_new.append(z * -1)
            elif z == y:
                number_new.append(z)
    print(number_new)    

    

checkio((-20, -5, 10, 15))

