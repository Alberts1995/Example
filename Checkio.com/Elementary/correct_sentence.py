def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    
    print(text)
correct_sentence("welcome to New York")


