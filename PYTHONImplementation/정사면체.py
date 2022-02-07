firstSide = [1, 0, 0, 0]
secondSide = [2, 3, 1, 2]
thirdSide = [3, 2, 3, 1]


roundNum = int(input())

for i in range(roundNum):
    firstLine = (input()).split()
    firstBoard, secondBoard = firstLine[:4], firstLine[4:]

    result = 0
    subFirst, subSecond = [], []
    for j in range(4):
        for k in range(4):

            if firstBoard[j] == secondBoard[k]:
                subFirst = [firstBoard[firstSide[j]], firstBoard[secondSide[j]], firstBoard[thirdSide[j]]]
                subSecond = [secondBoard[firstSide[k]], secondBoard[secondSide[k]], secondBoard[thirdSide[k]]]

                for l in range(3):
                    subNum = subSecond.pop(0)
                    subSecond.append(subNum)

                    for m in range(3):
                        if subFirst[m] == subSecond[m]:
                            if m == 2:
                                result = 1
                                break
                        else:
                            break
                    
                    if result == 1:
                        break
            if result == 1:
                break
        if result == 1:
            break

    print(result)