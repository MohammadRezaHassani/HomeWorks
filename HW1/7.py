inputStr = input()

myDict = {}

for i in range(len(inputStr)):
    repeted = 1
    for j in range(i+1,len(inputStr)):
        if inputStr[j]==inputStr[i]:
            repeted += 1

    if not inputStr[i] in myDict:
        myDict[inputStr[i]] = repeted

for key,value in myDict.items():
    print(key, ":", value)