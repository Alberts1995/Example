def index_power(array: list, n: int) -> int:
    if len(array) <= n:
        print(-1)
    elif len(array) > n:
        print(array[n] ** n)
    
   
index_power([1, 2], 3)

