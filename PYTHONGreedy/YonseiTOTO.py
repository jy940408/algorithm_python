subjectNum, mileageNum = map(int, (input()).split())

resultList = []
for i in range(subjectNum):
    subNum, fullNum = map(int, (input()).split())
    mileageList = (input()).split()
    
    scoreList = [0 for i in range(101)]
    for j in range(subNum):
        scoreList[int(mileageList[j])] += 1
        
    result = 0
    if subNum < fullNum:
        resultList.append(1)
    elif subNum >= fullNum:
        for j in range(100, 0, -1):
            result += scoreList[j]
            if result >= fullNum:
                resultList.append(j)
                break

resultList = sorted(resultList)
mileageSum = 0
result = 0
for i in range(subjectNum):
    mileageSum += resultList[i]
    if mileageSum > mileageNum:
        result = (i)
        break
    elif mileageSum == mileageNum:
        result = (i+1)
        break

if mileageNum > mileageSum:
    result = subjectNum

print(result)
