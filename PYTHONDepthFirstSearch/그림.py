import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList):
    global subResult
    subResult += 1

    visitList[heightRoot][widthRoot] = True

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if board[subHeight][subWidth] != 0 and not visitList[subHeight][subWidth]:
                dfs(subHeight, subWidth, board, visitList)

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
result = subResult = 0

firstLine = (input()).split()
height = int(firstLine[0])
width = int(firstLine[1])

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]
for i in range(height):
    secondLine = (input()).split()
    for j in range(width):
        board[i][j] = int(secondLine[j])

paintingNum = 0
for i in range(height):
    for j in range(width):
        if board[i][j] != 0 and not visitList[i][j]:
            paintingNum += 1
            subResult = 0
            dfs(i, j, board, visitList)
            if subResult >= result:
                result = subResult

print(str(paintingNum) + "\n" + str(result))