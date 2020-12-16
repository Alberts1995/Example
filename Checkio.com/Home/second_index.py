def second_index(text: str, symbol: str) -> [int, None]:
    a = 0
    b = -1
    for x in text:
        if text.count(symbol) >=2:
            b += 1
            if symbol == x:
                a += 1
                if a == 2:
                    print(b)
                    break
    print(None)




second_index("sims", "s")