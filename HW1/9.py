number = int(input())
print(1)
initialList = [1,1]

for i in range(number-1):
    print(initialList)
    changedList=[]
    changedList.append(1)
    for i in range(len(initialList)-1):
        x = initialList[i]+initialList[i+1]
        changedList.append(x)
    changedList.append(1)
    initialList = changedList



