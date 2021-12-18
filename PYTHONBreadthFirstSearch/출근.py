from collections import deque
import sys

def bfs(bfsDeque):
    global result, resultCheck, visitList

    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        for i in range(moveNum):
            subHeight = (thisDeque[0] + upDown[i])
            subWidth = (thisDeque[1] + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if board[subHeight][subWidth] == 1:
                    if visitList[subHeight][subWidth] == -1:
                        visitList[subHeight][subWidth] = (thisDeque[2]+1)
                        if subHeight == (height-1):
                            resultCheck = True
                            if result > visitList[subHeight][subWidth]:
                                result = visitList[subHeight][subWidth]
                        bfsDeque.append([subHeight, subWidth, visitList[subHeight][subWidth]])

resultCheck = False
result = 1e9

height, width = map(int, (sys.stdin.readline()).split())

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[-1 for i in range(width)] for i in range(height)]

bfsDeque = deque()
upDown = []
leftRight = []

for i in range(height):
    firstLine = (sys.stdin.readline()).split()
    for j in range(width):
        board[i][j] = int(firstLine[j])
        if i == 0 and board[i][j] == 1:
            bfsDeque.append([i, j, 0])

moveNum = int(sys.stdin.readline())
for i in range(moveNum):
    heightMove, widthMove = map(int, (sys.stdin.readline()).split())
    upDown.append(heightMove)
    leftRight.append(widthMove)

bfs(bfsDeque)

if resultCheck:
    print(result)
else:
    print(-1)