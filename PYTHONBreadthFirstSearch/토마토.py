from collections import deque

def bfs(bfsDeque, visitList):
    global board, result

    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        if result < thisDeque[2]:
            result = thisDeque[2]

        for i in range(4):
            subHeight = (thisDeque[0] + upDown[i])
            subWidth = (thisDeque[1] + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if board[subHeight][subWidth] == 0:
                    if not visitList[subHeight][subWidth]:
                        board[subHeight][subWidth] = 1
                        visitList[subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]    
result = 0

width, height = map(int, (input()).split())
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

bfsDeque = deque()
tomatoCheck = False
ripeCheck = False
for i in range(height):
    firstLine = (input()).split()
    for j in range(width):
        board[i][j] = int(firstLine[j])
        if board[i][j] == 1:
            bfsDeque.append([i, j, 0])
            tomatoCheck = True
        elif board[i][j] == 0:
            ripeCheck = True

resultCheck = True
if tomatoCheck and ripeCheck:
    bfs(bfsDeque, visitList)

    for i in range(height):
        for j in range(width):
            if board[i][j] == 0:
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
