import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList, colorCheck):
    visitList[heightRoot][widthRoot] = True

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < lineNum and subWidth < lineNum:
            if colorCheck == 1:
                if board[heightRoot][widthRoot] == board[subHeight][subWidth] and not visitList[subHeight][subWidth]:
                    dfs(subHeight, subWidth, board, visitList, colorCheck)
            else:
                if board[heightRoot][widthRoot] == "R" or board[heightRoot][widthRoot] == "G":
                    if board[subHeight][subWidth] != "B" and not visitList[subHeight][subWidth]:
                        dfs(subHeight, subWidth, board, visitList, colorCheck)
                else:
                    if board[heightRoot][widthRoot] == board[subHeight][subWidth] and not visitList[subHeight][subWidth]:
                        dfs(subHeight, subWidth, board, visitList, colorCheck)

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
lineNum = int(input())

board = [["0" for i in range(lineNum)] for i in range(lineNum)]
for i in range(lineNum):
    firstLine = input()
    for j in range(lineNum):
        board[i][j] = firstLine[j]

visitList = [[False for i in range(lineNum)] for i in range(lineNum)]
firstResult = 0
for i in range(lineNum):
    for j in range(lineNum):
        if not visitList[i][j]:
            dfs(i, j, board, visitList, 1)
            firstResult += 1

visitList = [[False for i in range(lineNum)] for i in range(lineNum)]
secondResult = 0
for i in range(lineNum):
    for j in range(lineNum):
        if not visitList[i][j]:
            dfs(i, j, board, visitList, -1)
            secondResult += 1

print(firstResult, secondResult)

