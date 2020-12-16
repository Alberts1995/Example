import re

def checkio(data):
    matchObj = re.match("[a-zA-Z0-9^\.]+", data)
    searchObjLetter = re.search("[a-z]+", data)
    searchObjUpLetter = re.search("[A-Z]+", data)
    searchObjNumber = re.search("[0-9]+", data)
    if len(data) >= 10:
        if matchObj:
            if searchObjLetter and searchObjUpLetter and searchObjNumber:
                print (True)
            else:
                print (False)
        else:
            print (False)
    else:
        print (False)


checkio("ULFFunH8ni")
