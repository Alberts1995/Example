lst = [7, 8, 9, 2, 1, 3, 5]
n = len(lst)

iteration = 0
for i in range(1, n):
    while i > 0 and lst[i] < lst[i - 1]:
        iteration += 1
        lst[i], lst[i-1] = lst[i-1], lst[i]
        i -=1

print(lst)
print(iteration)