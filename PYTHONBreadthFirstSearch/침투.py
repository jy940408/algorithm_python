from queue import Queue

def bfs(heightRoot, widthRoot):
    global trueCheck, visitList

    bfsQueue = Queue()
    bfsQueue.put([heightRoot, widthRoot])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisHeight = (thisQueue[0])
        thisWidth = (thisQueue[1])

        if thisHeight == (height-1):
            trueCheck = True
            return

        if not visitList[thisHeight][thisWidth]:
            visitList[thisHeight][thisWidth] = True

            for i in range(4):
                subHeight = (thisHeight + upDown[i])
                subWidth = (thisWidth + leftRight[i])
                if 0 <= subHeight < height and 0 <= subWidth < width:
                    if board[subHeight][subWidth] == 0:
                        if not visitList[subHeight][subWidth]:
                            bfsQueue.put([subHeight, subWidth])

trueCheck = False
upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]

height, width = map(int, (input()).split())
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = int(firstLine[j])

for i in range(width):
    if not visitList[0][i] and board[0][i] == 0:
        if not trueCheck:
            bfs(0, i)
        else:
            break

if trueCheck:
    print("YES")
else:
    print("NO")
