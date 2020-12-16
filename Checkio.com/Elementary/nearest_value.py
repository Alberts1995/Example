def nearest_value(values: set, one: int) -> int:
    print(min(values, key=lambda n: (abs(one - n), n)))

             
nearest_value([5,10,8,12,89,100],7)
