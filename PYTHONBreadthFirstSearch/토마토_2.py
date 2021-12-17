from collections import deque

def bfs(bfsDeque, visitList):
    global board, result

    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        if result < thisDeque[3]:
            result = thisDeque[3]

        for i in range(6):
            subHeight = (thisDeque[1] + upDown[i])
            subWidth = (thisDeque[2] + leftRight[i])
            subDepth = (thisDeque[0] + depthList[i])

            if 0 <= subHeight < height and 0 <= subWidth < width and 0 <= subDepth < depth:
                if board[subDepth][subHeight][subWidth] == 0:
                    if not visitList[subDepth][subHeight][subWidth]:
                        board[subDepth][subHeight][subWidth] = 1
                        visitList[subDepth][subHeight][subWidth] = True
                        bfsDeque.append([subDepth, subHeight, subWidth, (thisDeque[3]+1)])

upDown = [-1, 1, 0, 0, 0, 0]
leftRight = [0, 0, -1, 1, 0, 0]
depthList = [0, 0, 0, 0, -1, 1]    
result = 0

width, height, depth = map(int, (input()).split())
board = [[[0 for i in range(width)] for i in range(height)] for i in range(depth)]
visitList = [[[False for i in range(width)] for i in range(height)] for i in range(depth)]

bfsDeque = deque()
tomatoCheck = False
ripeCheck = False

for i in range(depth):
    for j in range(height):
        firstLine = (input()).split()
        for k in range(width):
            board[i][j][k] = int(firstLine[k])
            if board[i][j][k] == 1:
                bfsDeque.append([i, j, k, 0])
                tomatoCheck = True
            elif board[i][j][k] == 0:
                ripeCheck = True

resultCheck = True
if tomatoCheck and ripeCheck:
    bfs(bfsDeque, visitList)

    for i in range(depth):
        for j in range(height):
            for k in range(width):
                if board[i][j][k] == 0:
                    resultCheck = False
                    break

    if resultCheck and result != 0:
        print(result)
    elif resultCheck and result == 0:
        print(0)
    elif not resultCheck:
        print(-1)
elif not tomatoCheck and ripeCheck:
    print(-1)
elif tomatoCheck and not ripeCheck:
    print(0)