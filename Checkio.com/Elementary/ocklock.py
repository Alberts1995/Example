x = {"10":"10", "11":"11", "12":"12", "13":"1", "14":"2", 
    "15":"3", "16":"4", "17":"5", "18":"6", "19":"7", "20":"8", 
    "21":"9", "22":"10", "23":"11", 
    }

y = {"01":"1", "02":"2", "03":"3", 
    "04":"4", "05":"5", "06":"6",
    "07":"7", "08":"8", "09":"9",
    "00":"12",
    }

def time_converter(time):
    for key, value in x.items():
        if time[0:2] == key:
            print(value + time[2:] + " p.m.")
            break
    for key, value in y.items():
        if time[0:-3] == key:
            print(value + time[2:] +  " a.m.")


time_converter("00:15") 
