from copy import deepcopy
from itertools import product, permutations

def checkio(data):
    def operate(operator, a, b):
        if operator == 'A':
            return(a+b)
        elif operator == 'B':
            return (a-b)
        elif operator == 'C':
            return (a*b)
        elif operator == 'D':
            if b == 0:
                raise ValueError
            else:
                return (float(a)/b)
        raise ValueError

    for i in range(2**5):
        order = '%05d' % int(bin(i)[2:])
        numbers = []
        number = ''

        data_2 = deepcopy(data)
        for j in range(5):
            if not number:
                number = data_2[0]
                data_2 = data_2[1:]
            if int(order[j]):
                numbers.append(int(number))
                number = ''
            else:
                number += data_2[0]
                data_2 = data_2[1:]
            if not data_2:
                numbers.append(int(number))
                break
        if data_2:
            numbers.append(int(data_2))
        
        for j in product('ABCD', repeat=len(numbers)-1):
            for k in list(permutations(range(len(j)), len(j))):
                if not j and numbers[0] == 100:
                    return (False)
                if not j:
                    continue
                operations = list(j)
                operations_order = list(k)
                numbers_2 = deepcopy(numbers)

                while operations:
                    loc = operations_order.index(0)
                    try:
                        numbers_2[loc+1] = operate(operations[loc], numbers_2[loc], numbers_2[loc+1])
                    except:
                        break
                    numbers_2.pop(loc)
                    operations.pop(loc)
                    operations_order.pop(loc)
                    operations_order = [i-1 for i in operations_order]
                
                if abs(numbers_2[0]-100) < 0.01:
                    return (False)

    return (True)

checkio('271353')