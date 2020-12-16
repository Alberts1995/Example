def bigger_price(limit, data):
    print(sorted(data, key=lambda x: x['price'], reverse=True)[:limit])


bigger_price(3, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) 
