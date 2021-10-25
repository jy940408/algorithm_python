def dfs(heightRoot, widthRoot, board, resultList):

    if heightRoot == lineNum-1 and widthRoot == lineNum-1:

        global round
        round += 1
        subResult = int(resultList[0])
        for i in range (1, len(resultList)-1, 2):
            if resultList[i] == "+":
                subResult += int(resultList[i+1])
            elif resultList[i] == "-":
                subResult -= int(resultList[i+1])
            else:
                subResult *= int(resultList[i+1])

        global minResult
        global maxResult
        if round == 1:
            minResult = subResult
            maxResult = subResult
        else:
            if subResult <= minResult:
                minResult = subResult
            if subResult >= maxResult:
                maxResult = subResult

    for i in range(2):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + leftRight[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < lineNum and subWidth < lineNum:
            resultList.append(board[subHeight][subWidth])
            dfs(subHeight, subWidth, board, resultList)
            del resultList[len(resultList)-1]


maxResult = 0
minResult = 0
upDown = [1,0]
leftRight = [0,1]
round = 0

lineNum = int(input())
board = [["0" for i in range(lineNum)] for i in range(lineNum)]

for i in range(lineNum):
    firstLine = (input()).split()
    for j in range(lineNum):
        board[i][j] = firstLine[j]

resultList = []
resultList.append(board[0][0])
dfs(0, 0, board, resultList)

print(maxResult,minResult)