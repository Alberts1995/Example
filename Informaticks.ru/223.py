frs = input()
sec = list(map(int, input().split()))
third = int(input())


x = third
number = 0
for i in sec:
    if i == x:
        number += 1
    else:
        i > 0

print(number)
