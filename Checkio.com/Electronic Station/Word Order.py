def words_order(text: str, words: list) -> bool:
    new_words = text.split()
    newWords = []
    letter = {}
    z = 0
    for x in words:
        if x not in letter:
            letter[x] = 1
        else:
            letter[x] += 1

    for x in words:
        for y in new_words:
            z += 1
            if x == y:
                newWords.append(z)
                z *= 0
                break   
    
    for key, valuse in letter.items():
        if list(set(words) - set(new_words)) != []:
            print(False)
        elif newWords == sorted(newWords) and valuse < 2:
            print(True)
        else:
            print(False)

 

words_order("hi world im here",["country","here"])


