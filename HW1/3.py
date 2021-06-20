# Exercise 3

numList = list(map(int, input().split()))

maximum = 21
minimum = -1
totalSum = 0
for i in numList:
    totalSum += i
    if minimum == -1 or i < minimum:
        minimum = i
    if maximum == 21 or i > maximum:
        maximum = i
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", totalSum/len(numList))