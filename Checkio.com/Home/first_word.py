def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    print(text[0])

                

first_word("  Don't  dfs  sad")