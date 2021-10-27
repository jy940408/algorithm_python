import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList):

    global subResult, result
    subResult += 1
    visitList[heightRoot][widthRoot] = True

    if subResult >= result:
        result = subResult

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if board[subHeight][subWidth] == 1 and not visitList[subHeight][subWidth]:
                dfs(subHeight, subWidth, board, visitList)

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
subResult = result = 0

firstLine = (input()).split()
height = int(firstLine[0])
width = int(firstLine[1])
foodNum = int(firstLine[2])
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

for i in range(foodNum):
    secondLine = (input()).split()
    board[int(secondLine[0])-1][int(secondLine[1])-1] = 1

for i in range(height):
    for j in range(width):
        if board[i][j] == 1 and not visitList[i][j]:
            subResult = 0
            dfs(i, j, board, visitList)

print(result)