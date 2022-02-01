from collections import deque
import sys

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width, wallNum = map(int, (sys.stdin.readline()).split())

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[[-1 for i in range(width)] for i in range(height)] for i in range(wallNum+1)]
for i in range(height):
    firstLine = sys.stdin.readline()
    for j in range(width):
        board[i][j] = int(firstLine[j])

bfsDeque = deque()
bfsDeque.append([0, 0, 0, 1])

visitList[0][0][0] = 0
result = 0
resultCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == height-1 and thisDeque[1] == width-1:
        result = thisDeque[3]
        resultCheck = True
        break

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if board[subHeight][subWidth] == 0:
                if visitList[thisDeque[2]][subHeight][subWidth] == -1:
                    visitList[thisDeque[2]][subHeight][subWidth] = 0
                    bfsDeque.append([subHeight, subWidth, thisDeque[2], (thisDeque[3]+1)])
            else:
                if thisDeque[2] < wallNum:
                    if visitList[thisDeque[2]+1][subHeight][subWidth] == -1:
                        visitList[thisDeque[2]+1][subHeight][subWidth] = 0
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1), (thisDeque[3]+1)])

if resultCheck:
    print(result)
else:
    print(-1)