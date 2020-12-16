def date_time(time: str) -> str:
    manth = {"01":"January", "02":"February", "03":"March", 
            "04":"April", "05":"May", "06":"June", 
            "07":"July", "08":"August", "09":"September", 
            "10":"October", "11":"November", "12":"December"
            }
    all = {"00":"0", "01":"1", "02":"2", "03":"3", 
            "04":"4", "05":"5", "06":"6",
            "07":"7", "08":"8", "09":"9",
            }

    for key1, value1 in all.items():
        if key1 == time[0:2]:
            day = value1
            break
    for x in range(10, 61):
        if x == int(time[0:2]):
            day = x
            break
    for key2, value2 in all.items():
        if time[11:13] == "01":
            houre = "1 hour"
            break
        elif key2 == time[11:13]:
            houre = value2 + " hours"
            break
    for y in range(10, 61):
        if y == int(time[11:13]):
            houre = str(y) + " hours"
            break
    for key3, value3 in all.items():
        if time[14:16] == "01":
            minute = "1 minute"
            break
        elif key3 == time[14:16]:
            minute = value3 + " minutes"
            break
    for z in range(10, 61):
        if z == int(time[14:16]):
            minute = str(z) + " minutes"
            break
    for key, value in manth.items():
        if key == time[3:5]:
            print("{} {} {} year {} {}".format(day, value, time[6:10], houre, minute))
                    
date_time("09.05.1945 01:30") 