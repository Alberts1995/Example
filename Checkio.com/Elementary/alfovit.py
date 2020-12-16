def checkio(text):
    d = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
    s = sorted(d.items(), key=lambda item:(-item[1], item[0]))
    return print(s[0][0])


checkio("HhHheeell")

