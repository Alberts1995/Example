def sun_angle(time):
    d = -15.25
    for hour in range(6, 19):
        d += 15
        if hour == int(time[0:2]):
            break
        elif int(time[0:2]) >= 19 or int(time[0:2]) <= 5:
            print("I don't see the sun!")
            break
    for minute in range(0, 60):
        d += 0.25
        if int(time[0:2]) == 18 and minute+1 == int(time[3:]):
            print("I don't see the sun!")
            break
        elif minute == int(time[3:]):
            break        
    print(d)
   
sun_angle("18:01")




