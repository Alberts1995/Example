def backward_string_by_word(Sentence: str) -> str:
    words = Sentence.split(" ") 
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    print(newSentence)





backward_string_by_word("Hello   word")


