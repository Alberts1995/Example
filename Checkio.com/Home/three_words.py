def checkio(words: str) -> bool:
    d = 0
    for i in words.split():
        if d == 3:
            break
        elif i.isalpha():
            d += 1
        elif i.isdigit():
            d *= 0
    if d >= 3:
        print(True)
    else:
        print(False)

    
    

checkio("one two 3 four five six 7 eight 9 ten eleven 12")