import sys
from collections import deque

def bfs(heightRoot, widthRoot, visitList):
    global result

    bfsQueue = deque()
    bfsQueue.append([heightRoot, widthRoot, 0])
    visitList[heightRoot][widthRoot] = True

    while bfsQueue:
        thisQueue = bfsQueue.popleft()
        thisHeight = thisQueue[0]
        thisWidth = thisQueue[1]

        result = max(result, thisQueue[2])

        for i in range(4):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if not visitList[subHeight][subWidth] and board[subHeight][subWidth] == "L":
                    visitList[subHeight][subWidth] = True
                    bfsQueue.append([subHeight, subWidth, (thisQueue[2]+1)])

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

result = 0
height, width = map(int, (sys.stdin.readline()).split())
board = [list(sys.stdin.readline()) for i in range(height)]

for i in range(height):
    for j in range(width):
        if board[i][j] == "L":
            visitList = [[False for i in range(width)] for i in range(height)]
            bfs(i, j, visitList)

print(result)