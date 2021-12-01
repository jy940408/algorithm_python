from queue import Queue

def bfs(heightRoot, widthRoot, visitList):
    global result, resultCheck

    bfsQueue = Queue()
    bfsQueue.put([heightRoot, widthRoot, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisHeight = thisQueue[0]
        thisWidth = thisQueue[1]

        if thisHeight == goalHeight and thisWidth == goalWidth:
            result = thisQueue[2]
            resultCheck = True
            return

        for i in range(6):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            if 0 <= subHeight < length and 0 <= subWidth < length:
                if not visitList[subHeight][subWidth]:
                    visitList[subHeight][subWidth] = True
                    bfsQueue.put([subHeight, subWidth, (thisQueue[2]+1)])

upDown = [-2, -2, 0, 0, 2, 2]
leftRight = [-1, 1, -2, 2, -1, 1]

result = 0
resultCheck = False

length = int(input())
visitList = [[False for i in range(length)] for i in range(length)]
startHeight, startWidth, goalHeight, goalWidth = map(int, (input()).split())

bfs(startHeight, startWidth, visitList)

if resultCheck:
    print(result)
else:
    print(-1)