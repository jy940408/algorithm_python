testCase = int(input())

result = ""
for i in range(testCase):
    firstLine = input()
    lineSeperate = firstLine.split(" ")
    soldierNum = int(lineSeperate[0])
    soldierList = lineSeperate[1:]
    soldierSet = set(soldierList)
    soldierMap = dict()
    for i in soldierSet:
        soldierMap[i] = 0;

    for i in soldierList:
        soldierMap[i] += 1

    subResult = ""
    for i in soldierSet:
        if int(soldierMap[i]) > soldierNum//2:
            subResult += str(i) + "\n"
            result += subResult
    if subResult == "":
        result += "SYJKGW\n"

print(result)