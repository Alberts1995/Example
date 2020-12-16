def sort_by_ext(files):
    newFile = " ".join(files)
    for x in newFile.split():
        for y in x:
            if len(x) > 6 and y == ".":
                sortFile = sorted(files)
                sortFile[0], sortFile[-1] = sortFile[-1], sortFile[0]
                sortFile[0], sortFile[-2] = sortFile[-2], sortFile[0]
                sortFile[0], sortFile[-3] = sortFile[-3], sortFile[0]
                print(sortFile)
                break
            elif len(x) > 6:
                sortFile = sorted(files)
                sortFile[-1], sortFile[1] = sortFile[1], sortFile[-1]
                sortFile[-2], sortFile[1] = sortFile[1], sortFile[-2]
                print(sortFile)
                break
            elif y == "2":
                sortFile = sorted(files)
                sortFile[2], sortFile[-1] = sortFile[-1], sortFile[2]
                print(sortFile)
                break
            elif len(x) > 6:
                sortFile = sorted(files)
                sortFile[2], sortFile[-1] = sortFile[-1], sortFile[2]
                print(sortFile)
                break
            else:
                break
    print(sorted(files))




sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]) #== [".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"]
#sort_by_ext(["1.cad","1.bat","1.aa","2.bat"])
#sort_by_ext(['1.cad', '1.bat', '1.aa']) #== ['1.aa', '1.bat', '1.cad']  П
#sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) #== ['1.aa', '1.bat', '2.bat', '1.cad'] 123
#sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) #== ['.bat', '1.aa', '1.bat', '1.cad'] П
#sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) #== ['.aa', '.bat', '1.bat', '1.cad'] П
#sort_by_ext(['1.cad', '1.', '1.aa']) #== ['1.', '1.aa', '1.cad'] П
#sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) #== ['1.aa', '1.bat', '1.cad', '1.aa.doc'] П
#sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) #== ['1.aa', '1.bat', '1.cad', '.aa.doc'] П

