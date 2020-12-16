lst = list(range(10))
need = 3

left = 0
right = len(lst) -1 
iteration = 0
while left <= right:
    iteration += 1
    med = (left + right) // 2
    if lst[med] > need:
        right = med - 1
    elif lst[med] < need:
        left = med + 1 
    else:
        print(f"Found {iteration} iteration")
        break
else:
    print(f"not found {iteration} iteration")

