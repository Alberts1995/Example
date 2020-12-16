def end_zeros(num: int) -> int:
    a = 0
    for number in str(num):
        if number == "0":
            a +=1
        elif number != "0":
            a *=0
    print(int(a))
end_zeros(10)
