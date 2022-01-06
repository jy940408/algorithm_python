month = int(input())
silver, gold, platinum, diamond = map(int, (input()).split())
payList = [silver, gold, platinum, diamond]

gradeList = []
grade = input()
for i in range(month):
    if grade[i] == "B":
        gradeList.append(0)
    elif grade[i] == "S":
        gradeList.append(1)
    elif grade[i] == "G":
        gradeList.append(2)
    elif grade[i] == "P":
        gradeList.append(3)
    elif grade[i] == "D":
        gradeList.append(4)

result = 0
preMonth = 0
for i in range(month):
    if i == 0:
        if gradeList[i] == 4:
            result += payList[3]
        else:
            result += (payList[gradeList[i]]-1)
            preMonth = (payList[gradeList[i]]-1)
    else:
        if gradeList[i] == 4:
            result += payList[3]
        else:
            result += ((payList[gradeList[i]]-1)-preMonth)
            preMonth = ((payList[gradeList[i]]-1)-preMonth)

print(result)