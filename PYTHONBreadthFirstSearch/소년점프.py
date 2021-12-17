from collections import deque

def bfs(personIdx, heightRoot, widthRoot):
    global visitLength

    bfsDeque = deque()
    bfsDeque.append([heightRoot, widthRoot, 0])

    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        for i in range(4):
            subHeight = (thisDeque[0] + upDown[i])
            subWidth = (thisDeque[1] + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if board[subHeight][subWidth] == 0:
                    if visitLength[subHeight][subWidth][personIdx] == -1:
                        visitLength[subHeight][subWidth][personIdx] = (thisDeque[2] + 1)
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, (input()).split())
board = [[0 for i in range(width)] for i in range(height)]
visitLength = [[[-1]*3 for i in range(width)] for i in range(height)]

for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = int(firstLine[j])

for i in range(3):
    startHeight, startWidth = map(int, (input()).split())
    visitLength[(startHeight-1)][(startWidth-1)][i] = 0
    bfs(i, (startHeight-1), (startWidth-1))

resultTime = 1e9
resultNum = 0
for i in range(height):
    for j in range(width):
        goalTime = max(visitLength[i][j])
        if min(visitLength[i][j]) != -1:
            if resultTime > goalTime:
                resultTime = goalTime
                resultNum = 1
            elif resultTime == goalTime:
                resultNum += 1

if resultNum != 0:
    print(resultTime)
    print(resultNum)
else:
    print(-1)

