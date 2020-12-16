def max_digit(number: int) -> int:
    s = str(number)
    ls = list(map(int, s))
    r = max(ls)
    print(r)
max_digit(345)