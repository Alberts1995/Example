def beginning_zeros(number: str) -> int:
    b = 0
    for i in number:
        if i == "0":
            b += 1
        else:
            break
    print(b)

beginning_zeros("100")