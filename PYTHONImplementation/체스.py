upDown = [-1, -1, 1, 1]
leftRight = [-1, 1, -1, 1]

roundNum = int(input())

for i in range(roundNum):
    firstLine = list(map(str, input().split()))
    startWidth, startHeight = (ord(firstLine[0])-64), int(firstLine[1])
    goalWidth, goalHeight = (ord(firstLine[2])-64), int(firstLine[3])

    midRoot = [0, 0]
    resultCheck = False
    for i in range(0, 9):
        for j in range(4):

            if 1 <= (startHeight+(i*upDown[j])) < 9 and 1 <= (startWidth+(i*leftRight[j])) < 9:
                if abs(goalHeight - (startHeight+(i*upDown[j]))) == abs(goalWidth - (startWidth+(i*leftRight[j]))):
                    midRoot = [(startHeight+(i*upDown[j])), (startWidth+(i*leftRight[j]))]
                    resultCheck = True
                    break

        if resultCheck:
            break

    if resultCheck:
        if startWidth == goalWidth and startHeight == goalHeight:
            print(0, chr(startWidth+64), startHeight)
        elif startWidth == midRoot[1] and startHeight == midRoot[0]:
            print(1, chr(startWidth+64), startHeight, chr(goalWidth+64), goalHeight)
        else:
            print(2, chr(startWidth+64), startHeight, chr(midRoot[1]+64), midRoot[0], chr(goalWidth+64), goalHeight)
    else:
        print("Impossible")