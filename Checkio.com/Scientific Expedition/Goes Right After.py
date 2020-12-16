def goes_after(word: str, first: str, second: str) -> bool:
    a = 0
    z = 0
    q = 0
    for x in word:
        a += 1
        if x == "":
            print(False)
        if x == second:
            q += 1
        elif x == first:
            for y in word[a::]:
                z += 1
                if z <= 1:
                    if y == second and q == 0:
                        print(True)
                        break
    print(False)


goes_after("panorama","a","n")
#goes_after("almaz","m","a")
#goes_after("world","l","o")
#goes_after('world', 'w', 'o') #== True
#goes_after('listo', 'l', 'o') #== False