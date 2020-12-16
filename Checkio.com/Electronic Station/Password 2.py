def is_acceptable_password(password: str) -> bool:
    for x in password:
        if x.isdigit() and len(password) > 6:
            print(True)
    print(False)

is_acceptable_password("muchlong1er")
