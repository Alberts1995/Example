def left_join(phrases):
    w = []
    for i in phrases:
        w.append(i.replace("right", "left"))
    print (','.join (w))



left_join(("left", "aright", "left", "stop"))


