lst = [7, 8, 9, 2, 1, 3, 5]
n = len(lst)
iter = 0
for i in range(n-1):
    for j in range(n-1-i):
        if lst[j] > lst[j+1]:
            iter += 1
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)
print(iter)  