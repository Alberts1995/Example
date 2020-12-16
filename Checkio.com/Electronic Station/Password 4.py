def is_acceptable_password(password: str) -> bool:
    for x in password:
        if len(password) >9:
            print(True)
            break
        elif x.isdigit() and len(password) > 6:
            for x in password:
                if x.isalpha():
                    print(True)
                    break

    print(False)

is_acceptable_password("muchlonger5")
