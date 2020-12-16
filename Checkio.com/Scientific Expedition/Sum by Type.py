def sum_by_types(items):
    word  = ""
    number = 0
    for i in items:
        if i == str(i):
            word += i
        else:
            number += i
    print(word, number)





#sum_by_types([]) #== ('', 0)
#sum_by_types([1, 2, 3]) #== ('', 6)
#sum_by_types(['1', 2, 3]) #== ('1', 5)
#sum_by_types(['1', '2', 3]) #== ('12', 3)
sum_by_types(['1', '2', '3']) #== ('123', 0)