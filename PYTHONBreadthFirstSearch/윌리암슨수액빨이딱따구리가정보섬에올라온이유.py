from collections import deque
import sys

def bfs(startHeight, startWidth, visitList):
    global result, resultCheck

    bfsQueue = deque()
    bfsQueue.append([startHeight, startWidth, 0])

    while bfsQueue:
        thisQueue = bfsQueue.popleft()
        thisHeight = thisQueue[0]
        thisWidth = thisQueue[1]

        for i in range(4):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if not visitList[subHeight][subWidth] and board[subHeight][subWidth] != 1:
                    if board[subHeight][subWidth] == 3 or board[subHeight][subWidth] == 4 or board[subHeight][subWidth] == 5:
                        result = (thisQueue[2]+1)
                        resultCheck = True
                        return
                    visitList[subHeight][subWidth] = True
                    bfsQueue.append([subHeight, subWidth, (thisQueue[2]+1)])

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

result = 0
resultCheck = False
startHeight = startWidth = 0

height, width = map(int, (sys.stdin.readline()).split())
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

for i in range(height):
    firstLine = sys.stdin.readline()
    for j in range(width):
        board[i][j] = int(firstLine[j])
        if board[i][j] == 2:
            startHeight = i
            startWidth = j

bfs(startHeight, startWidth, visitList)

if resultCheck:
    print("TAK")
    print(result)
else:
    print("NIE")