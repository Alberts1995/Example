def is_acceptable_password(password: str) -> bool:
    b = ""
    d = {}
    # если в конце или начале есть слово password
    for x in password.split():
        if x.lower() == "password":
            print(False)
            break
    # если слово целиком состоит из password и любого другого
    for x in password:
        if x.isalpha():
            b += x
            if b.lower() == "password":
                print(False)
                break
        elif x.isdigit():
            break
    for x in password:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    # Если слово больше 9 знаков                   
    for x in password:
        if len(password) > 9 and len(d) >= 3:
            print(True)
            break
    # Если больше 6 и есть хоть одна цифра
    for x in password:
        if x.isdigit() and len(password) > 6 and len(d) >= 3 :
            for x in password:
                if x.isalpha():
                    print(True)
                    break

    print(False)

is_acceptable_password("aaaaaabb1")
