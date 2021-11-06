import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList):

    visitList[heightRoot][widthRoot] = True

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if board[subHeight][subWidth] == 255 and not visitList[subHeight][subWidth]:
                dfs(subHeight, subWidth, board, visitList)



upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]

firstLine = (input()).split()
height = int(firstLine[0])
width = int(firstLine[1])
redBoard = [[0 for i in range(width)] for i in range(height)]
greenBoard = [[0 for i in range(width)] for i in range(height)]
blueBoard = [[0 for i in range(width)] for i in range(height)]

for i in range(height):
    secondLine = (input()).split()
    redNum = 0
    greenNum = 1
    blueNum = 2
    for j in range(width):
        redBoard[i][j] = int(secondLine[redNum])
        redNum += 3
        greenBoard[i][j] = int(secondLine[greenNum])
        greenNum  += 3
        blueBoard[i][j] = int(secondLine[blueNum])
        blueNum += 3

standard = int(input())
board = [[0 for i in range(width)] for i in range(height)]
for i in range(height):
    for j in range(width):
        sum = (redBoard[i][j] + greenBoard[i][j] + blueBoard[i][j])//3
        if standard <= sum:
            board[i][j] = 255
        elif standard > sum:
            board[i][j] = 0

visitList = [[False for i in range(width)] for i in range(height)]
result = 0
for i in range(height):
    for j in range(width):
        if board[i][j] == 255 and not visitList[i][j]:
            result += 1
            dfs(i, j, board, visitList)

print(result)
