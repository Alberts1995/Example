def split_pairs(a):
    len(a)
    w = []
    for i in a:
        if len(a) == 4:
            w.append(a[0:2])
            w.append(a[2:4])
            break
        elif len(a) == 3:
            w.append(a[0:2])
            w.append(a[2:] + "_")
            break
        elif len(a) == 2:
            w.append(a[0:2])
            break
        elif len(a) == 1:
            w.append(a[0:1]+ "_")
            break
        elif len(a) == 5:
            w.append(a[0:2])
            w.append(a[2:4])
            w.append(a[4:] + "_")
            break
        
    print(w)
split_pairs("abcda")

