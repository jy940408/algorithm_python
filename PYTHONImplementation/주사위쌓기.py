
diceCheck = {0 : 5, 1 : 3, 2: 4, 3: 1, 4: 2, 5: 0}
diceNum = int(input())
diceList = [[] for i in range(diceNum)]

for i in range(diceNum):
    firstLine = (input()).split()
    for j in firstLine:
        diceList[i].append(int(j))

result = 0
for i in range(6):
    
    thisDice = 0
    for k in range(6):
        if k != i and k != diceCheck.get(i):
            thisDice = max(thisDice, diceList[0][k])
    subResult = thisDice
    preDice = diceList[0][diceCheck.get(i)]

    for j in range(1, diceNum):
        
        idx = 0
        for k in range(6):
            if diceList[j][k] == preDice:
                idx = k
        
        thisDice = 0
        for k in range(6):
            if k != idx and k != diceCheck.get(idx):
                print(j, k, "thisDice:",thisDice, "diceList[j][k]:",diceList[j][k])
                thisDice = max(thisDice, diceList[j][k])
        
        print(i, j, "idx:", idx, "diceCheck.get(idx):", diceCheck.get(idx), "thisDice:",thisDice)

        subResult += thisDice
        preDice = diceList[j][diceCheck.get(idx)]

    print("subResult:",subResult)
    result = max(result, subResult)

print(result)
print(diceList)