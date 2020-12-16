def popular_words(text: str, words: list) -> dict:
    a = " ".join(words)
    d = {i : 0 for i in words}
    for letter in text.split():
        for x in a.split():
            if letter.upper() == x.upper():
                d[x] += 1

    print(d)


popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ["one","two","three"])


