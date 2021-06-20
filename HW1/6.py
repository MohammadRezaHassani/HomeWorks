inputList = input()
firstNum = 0
secondNum = 0


def extractexp(inputlist):
    fnum = 0
    snum = 0
    for i in range(len(inputList)):
        if i+1<len(inputlist):
            if not inputList[i + 1].isdigit() and inputList[i].isdigit():
                fnum = int(inputList[: i + 1])
            if inputList[i + 1].isdigit() and not inputList[i].isdigit():
                snum = int(inputList[i + 1:])

    return fnum, snum


if "*" in inputList:
    firstNum, secondNum = extractexp(inputList)
    print("Result: ", firstNum * secondNum)
elif "-" in inputList:
    firstNum, secondNum = extractexp(inputList)
    print("Result: ", firstNum - secondNum)
elif "+" in inputList:
    firstNum, secondNum = extractexp(inputList)
    print("Result: ", firstNum + secondNum)
else:
    firstNum, secondNum = extractexp(inputList)
    print("Result: ", firstNum / secondNum)
