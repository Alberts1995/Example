def is_acceptable_password(password: str) -> bool:
    if len(password) > 6: 
        print(True)
    else:
        print(False)

is_acceptable_password("muchlonger")

