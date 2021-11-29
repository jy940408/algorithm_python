from queue import Queue

def bfs(heightRoot, widthRoot, visitList):
    global wResult, bResult

    bfsQueue = Queue()
    bfsQueue.put([heightRoot, widthRoot, 1])
    visitList[heightRoot][widthRoot] = True

    numCheck = 0
    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisHeight = thisQueue[0]
        thisWidth = thisQueue[1]

        if board[thisHeight][thisWidth] == board[heightRoot][widthRoot]:
            numCheck += 1

        for i in range(4):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if board[subHeight][subWidth] == board[heightRoot][widthRoot]:
                    if not visitList[subHeight][subWidth]:
                        visitList[subHeight][subWidth] = True
                        bfsQueue.put([subHeight, subWidth, (thisQueue[2] + 1)])

    if board[heightRoot][widthRoot] == "W":
        wResult += (numCheck**2)
    else:
        bResult += (numCheck**2)

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]

wResult = 0
bResult = 0

width, height = map(int, (input()).split())
board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

for i in range(height):
    for j in range(width):
        if not visitList[i][j]:
            bfs(i, j, visitList)

print(wResult, bResult)
