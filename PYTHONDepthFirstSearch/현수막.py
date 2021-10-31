import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList):
    visitList[heightRoot][widthRoot] = True

    for i in range(8):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if board[subHeight][subWidth] != 0 and not visitList[subHeight][subWidth]:
                dfs(subHeight, subWidth, board, visitList)

upDown = [-1,1,0,0,-1,-1,1,1]
leftRight = [0,0,-1,1,-1,1,-1,1]

firstLine = (input()).split()
height = int(firstLine[0])
width = int(firstLine[1])
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]
for i in range(height):
    secondLine = (input()).split()
    for j in range(width):
        board[i][j] = int(secondLine[j])

result = 0
for i in range(height):
    for j in range(width):
        if board[i][j] != 0 and not visitList[i][j]:
          result += 1
          dfs(i, j, board, visitList)

print(result)