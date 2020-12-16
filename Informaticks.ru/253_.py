c = int(input())
if (c%4==0  and c%100!=0) or (c%400 == 0):
    print("YES")
else:
    print("NO")   
