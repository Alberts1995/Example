def translate(data):
    a = 0
    Glas = "aeiouy"
    Soglas = "bcdfghjklmnpqrstvwxz"
    word = ""
    for i in data:
        try:
            if i == " ":
                a += 1
                word += i
            elif i == data[a]:
                for x in Soglas:
                    if i == x:
                        word += i
                        a += 2
                        break
                for y in Glas:
                    if y == i:
                        word += i
                        a += 3
                        break
        except:
            print(word)
            

#translate("aaa bo cy da eee fe") == "a b c d e f"    
translate("hoooowe yyyooouuu duoooiiine") #how you doin
#translate("hieeelalaooo") #== "hello", "Hi!"