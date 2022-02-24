def splitCheck(testCase):
    splitResult = []
    subResult = ""
    for i in testCase:
        if i == "S" or i == "M" or i == "U" or i == "P" or i == "C":
            if subResult != "":
                splitResult.append(int(subResult))
            subResult = ""
        else:
            subResult += i

    return splitResult

symbolNum = int(input())
testCase = list(input())

splitList = splitCheck(testCase)
numberIdx = 1
result = ""
subResult = splitList[0]
for i in testCase:

    if i == "C":
        result += (str(subResult) + " ")
    else:
        if len(splitList) > numberIdx:
            if i == "S":
                subResult -= splitList[numberIdx]
                numberIdx += 1
            elif i == "M":
                subResult *= splitList[numberIdx]
                numberIdx += 1
            elif i == "U":
                if subResult < 0:
                    subResult = -1*((-1*subResult)//splitList[numberIdx])
                else:
                    subResult //= splitList[numberIdx]
                numberIdx += 1
            elif i == "P":
                subResult += splitList[numberIdx]
                numberIdx += 1
    
if result == "":
    print("NO OUTPUT")
else:
    print(result)