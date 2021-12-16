from collections import deque
import sys

def bfs(bfsDeque):
    global visitList, result

    while bfsDeque:
        thisDeque = bfsDeque.popleft()
        thisHeight = thisDeque[0]
        thisWidth = thisDeque[1]

        for i in range(8):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if visitList[subHeight][subWidth] == -1:
                    if board[subHeight][subWidth] == 0:
                        visitList[subHeight][subWidth] = (thisDeque[2]+1)
                        if result < visitList[subHeight][subWidth]:
                            result = visitList[subHeight][subWidth]
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2] + 1)])

result = 0

upDown = [-1,-1,-1,0,0,1,1,1]
leftRight = [-1,0,1,-1,1,-1,0,1]

height, width = map(int, (sys.stdin.readline()).split())
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[-1 for i in range(width)] for i in range(height)]

bfsDeque = deque()
for i in range(height):
    firstLine = (sys.stdin.readline()).split()
    for j in range(width):
        board[i][j] = int(firstLine[j])
        if board[i][j] == 1:
            bfsDeque.append([i, j, 0])

bfs(bfsDeque)

for i in range(height):
    print(visitList[i])

print(result)