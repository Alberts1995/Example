def between_markers(text: str, begin: str, end: str) -> str:
    s, e = text.find(begin), text.find(end)
    print(text[(s+len(begin), None)[s == -1]: (e, None)[e == -1]])


between_markers('What is >apple<', '>', '<')