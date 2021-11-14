def bt(ingredientsList, visitList, root):
    global thisProtein, thisFat, thisCarbs, thisVitamin, thisPrice, resultPrice, resultList, subList

    if thisProtein >= minProtein and thisFat >= minFat and thisCarbs >= minCarbs and thisVitamin >= minVitamin:
        if thisPrice < resultPrice:
            resultPrice = thisPrice
            resultList = subList.copy()
        elif thisPrice == resultPrice:
            standard = ""
            compare = ""
            for i in range(len(resultList)):
                standard += str(resultList[i])
            for i in range(len(subList)):
                compare += str(subList[i])

            if standard > compare:
                resultPrice = thisPrice
                resultList = subList.copy()
        return

    for i in range(len(ingredientsList)):
        if i >= root:
            if not visitList[i]:
                visitList[i] = True

                subList.append((i+1))
                thisProtein += int(ingredientsList[i][0])
                thisFat += int(ingredientsList[i][1])
                thisCarbs += int(ingredientsList[i][2])
                thisVitamin += int(ingredientsList[i][3])
                thisPrice += int(ingredientsList[i][4])

                bt(ingredientsList, visitList, i)

                subList.pop(len(subList)-1)
                thisProtein -= int(ingredientsList[i][0])
                thisFat -= int(ingredientsList[i][1])
                thisCarbs -= int(ingredientsList[i][2])
                thisVitamin -= int(ingredientsList[i][3])
                thisPrice -= int(ingredientsList[i][4])

                visitList[i] = False


resultPrice = 7500
resultList = []
subList = []
result = ""

ingredientsNum = int(input())
minProtein, minFat, minCarbs, minVitamin = map(int, (input()).split())
thisProtein = thisFat = thisCarbs = thisVitamin = thisPrice = 0
ingredientsList = []

for i in range(ingredientsNum):
    ingredientsList.append((input()).split())
visitList = [False for i in range(len(ingredientsList))]

bt(ingredientsList, visitList, 0)

if len(resultList) == 0:
    print(-1)
else:
    for i in range(len(resultList)):
        result += str(resultList[i]) + " "

    print(resultPrice)
    print(result)