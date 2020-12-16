def first_word(text: str) -> str:
    myList  = []
    for leter in text:
        if leter == " ":
            break
        else:
            myList.append(leter)
    myString = ''.join(myList)
    print(myString)

first_word("adsad World")

