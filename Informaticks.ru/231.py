input()
sec = list(map(int, input().split()))
third = list(map(int, input().split()))

sec.insert(third[1]-1, third[0])
print(*sec)