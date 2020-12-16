def is_ascending(items):
    if items == []:
        print(True)
    letter = {}
    for x in items:
        if x not in letter:
            letter[x] = 1
        else:
            letter[x] += 1
        
    for key, value in letter.items():
        if sorted(items) == items and value < 2:
            print(True)
            break
        else:
            print(False)
            break


is_ascending([1, 1, 1, 1])


