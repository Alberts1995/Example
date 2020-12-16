from collections import defaultdict

def frequency_sort(lis):    
    dic = defaultdict(int)
    for num in lis:
        dic[num] += 1

    s_list = sorted(dic, key=dic.__getitem__, reverse=True)

    new_list = []
    for num in s_list:
        for rep in range(dic[num]):
            new_list.append(num)

    print(new_list)


frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) ##== [4, 4, 4, 4, 6, 6, 2, 2]


