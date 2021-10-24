import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board):
    visitList[heightRoot][widthRoot] = True

    for i in range(4):
        subHeight = (heightRoot + upDown[i])
        subWidth = (widthRoot + rightLeft[i])

        if subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width:
            if board[subHeight][subWidth] == 1 and not visitList[subHeight][subWidth]:
                dfs(subHeight, subWidth, board)

upDown = [-1, 1, 0, 0]
rightLeft = [0, 0, -1, 1]
testCase = int(input())

for i in range(testCase):
    firstLine = (input()).split(" ")
    width = int(firstLine[0])
    height = int(firstLine[1])

    cabbageNum = int(firstLine[2])
    board = [[0 for j in range(width)] for k in range(height)]
    visitList = [[False for j in range(width)] for k in range(height)]

    for j in range(cabbageNum):
        secondLine = (input()).split(" ")
        cabbageWidth = int(secondLine[0])
        cabbageHeight = int(secondLine[1])
        board[cabbageHeight][cabbageWidth] = 1

    result = 0;
    for j in range(height):
        for k in range(width):
            if board[j][k] == 1 and not visitList[j][k]:
                dfs(j, k, board);
                result += 1

    print(result)