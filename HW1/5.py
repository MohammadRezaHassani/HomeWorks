List1 = ["morning", "aftenoon", "night"]
List2 = ["Saturday", "Sunday", "Monday", "Tuesda", "Wednesday", "Thursday", "Friday"]

resList = []

for i in List2:
    for j in List1:
        L = i + "-" + j
        resList.append(L)
print(resList)
