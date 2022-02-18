upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]
sideCheck = [1, 0, 3, 2]
markList = ["|", "-", "+", "1", "2", "3", "4", "M", "Z"]
markSideList = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1]]


height, width = map(int, input().split())
board = [[[0 for i in range(4)] for i in range(width)] for i in range(height)]
originBoard = [["" for i in range(width)] for i in range(height)]

result = ""
resultLocation = [-1, -1]
for i in range(height):
    firstLine = input()
    for j in range(width):
        originBoard[i][j] = firstLine[j]

        for k in range(9):
            if firstLine[j] == markList[k]:
                board[i][j] = markSideList[k]
                break

for i in range(height):
    for j in range(width):
        subList = [0, 0, 0, 0]
        subCheck = 0
        mLocation = -1
        zLocation = -1
        if originBoard[i][j] == ".":
            for k in range(4):
                subHeight = (i + upDown[k])
                subWidth = (j + leftRight[k])

                if 0 <= subHeight < height and 0 <= subWidth < width:
                    subList[k] = board[subHeight][subWidth][sideCheck[k]]
                    
                    if originBoard[subHeight][subWidth] == "M":
                        mLocation = k
                    elif originBoard[subHeight][subWidth] == "Z":
                        zLocation = k

                    if subList[k] == 1:
                        subCheck += 1

        if mLocation != -1 and zLocation != -1:
            subList[mLocation] = 0
            subList[zLocation] = 0

        if subCheck > 1:
            for k in range(7):
                if subList == markSideList[k]:
                    result = markList[k]
                    resultLocation = [i, j]
                    break

print((resultLocation[0]+1), (resultLocation[1]+1), result)