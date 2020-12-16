def is_acceptable_password(password: str) -> bool:
    b = ""
    for x in password.split():
        if x.lower() == "password":
            print(False)
            break
    for x in password:
        if x.isalpha():
            b += x
            if b.lower() == "password":
                print(False)
                break
        elif x.isdigit():
            break
    for x in password:
        if len(password) > 9:
            print(True)
            break
        elif x.isdigit() and len(password) > 6:
            for x in password:
                if x.isalpha():
                    print(True)
                    break

    print(False)

is_acceptable_password("pass1234word")
