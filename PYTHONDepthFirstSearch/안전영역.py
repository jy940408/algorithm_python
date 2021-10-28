import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList, height):
    visitList[heightRoot][widthRoot] = True

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < lineNum and subWidth < lineNum:
            if board[subHeight][subWidth] > height and not visitList[subHeight][subWidth]:
                dfs(subHeight, subWidth, board, visitList, height)

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
result = height = subResult = 0
lineNum = int(input())
board = [[0 for i in range(lineNum)] for i in range(lineNum)]
visitList = [[False for i in range(lineNum)] for i in range(lineNum)]

for i in range(lineNum):
    firstLine = (input()).split()
    for j in range(lineNum):
        if int(firstLine[j]) >= height:
            height = int(firstLine[j])
        board[i][j] = int(firstLine[j])

for k in range(height):
    subResult = 0
    visitList = [[False for i in range(lineNum)] for i in range(lineNum)]
    for i in range(lineNum):
        for j in range(lineNum):
            if board[i][j] > k and not visitList[i][j]:
                subResult += 1
                dfs(i, j, board, visitList, k)
    if subResult >= result:
        result = subResult

print(result)
