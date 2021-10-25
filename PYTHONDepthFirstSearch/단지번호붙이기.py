def dfs(heightRoot, widthRoot, board, visitList):
    visitList[heightRoot][widthRoot] = True
    global result
    result += 1
    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < lineNum and subWidth < lineNum:
            if board[subHeight][subWidth] == 1 and not visitList[subHeight][subWidth]:
                dfs(subHeight, subWidth, board, visitList);

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
result = 0
resultList = []

lineNum = int(input())
board = [[0 for i in range(lineNum)] for j in range(lineNum)]
visitList = [[False for i in range(lineNum)] for j in range(lineNum)]

for i in range(lineNum):
    firstLine = input()
    for j in range(lineNum):
        board[i][j] = int(firstLine[j])

for i in range(lineNum):
    for j in range(lineNum):
        if board[i][j] == 1 and not visitList[i][j]:
            dfs(i, j, board, visitList)
            resultList.append(result)
            result = 0

resultList.sort()

print(len(resultList))
for i in range(len(resultList)):
    print(resultList[i])