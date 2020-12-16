def isometric_strings(str1: str, str2: str) -> bool:
    checklist = {}
    for i in range(len(str1)):
        if str1[i] not in checklist.keys():
            checklist[str1[i]] = str2[i]
        else:
            if str2[i] != checklist[str1[i]]:
                print(False)
    print(True)

isometric_strings('foo', 'bar')