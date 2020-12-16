def checkio(data: list) -> list:
    print([i for i in data if data.count(i) > 1])
checkio([1, 3, 1, 5, 1])