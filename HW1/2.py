# Exercise 2

vowels = ['a', 'e', 'i', 'o', 'u']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
inputStr = input()
vowelsNum = 0
digitsNum = 0
digitsSum = 0
repeatedCharDict = {}

for i in range(len(inputStr)):
    character = inputStr[i]
    charNum = 1
    if character.lower() in vowels:
        vowelsNum += 1
    if character in numbers:
        digitsNum += 1
        digitsSum += int(character)
    for j in range(i+1,len(inputStr)):
        if inputStr[j] == character:
            charNum += 1
    if charNum > 1 and character not in repeatedCharDict:
        repeatedCharDict[character] = charNum

print("Vowels:", vowelsNum)
print("Digits:", digitsNum)
print("Sum of digits:", digitsSum)
print(repeatedCharDict)
