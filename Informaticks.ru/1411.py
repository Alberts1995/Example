firs = input()
sec = list(map(int, input().split()))
n = len(sec)
iter = 0


for i in range(n-1):
    for j in range(n-1-i):
        if sec[j] > sec[j+1]:
            iter += 1
            sec[j], sec[j+1] = sec[j+1], sec[j]

print(iter)
