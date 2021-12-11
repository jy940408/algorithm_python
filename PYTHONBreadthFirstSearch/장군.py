from collections import deque

def bfs(startHeight, startWidth, goalHeight, goalWidth, visitList):
    global result, resultCheck

    bfsDeque = deque()
    bfsDeque.append([startHeight, startWidth, 0])

    while bfsDeque:
        thisDeque = bfsDeque.popleft()
        thisHeight = thisDeque[0]
        thisWidth = thisDeque[1]

        for i in range(8):
            subHeight = (thisHeight + upDown[i])
            subWidth = (thisWidth + leftRight[i])

            roadCheck = True
            if i == 0 or i == 1:
                if (subHeight+1) == goalHeight and (subWidth+1) == goalWidth:
                    roadCheck = False
                elif (subHeight+2) == goalHeight and (subWidth+2) == goalWidth:
                    roadCheck = False
            elif i == 2 or i == 3:
                if (subHeight+1) == goalHeight and (subWidth-1) == goalWidth:
                    roadCheck = False
                elif (subHeight+2) == goalHeight and (subWidth-2) == goalWidth:
                    roadCheck = False
            elif i == 4 or i == 5:
                if (subHeight-1) == goalHeight and (subWidth+1) == goalWidth:
                    roadCheck = False
                elif (subHeight-2) == goalHeight and (subWidth+2) == goalWidth:
                    roadCheck = False
            else:
                if (subHeight-1) == goalHeight and (subWidth-1) == goalWidth:
                    roadCheck = False
                elif (subHeight-2) == goalHeight and (subWidth-2) == goalWidth:
                    roadCheck = False

            if roadCheck:
                if 0 <= subHeight < 10 and 0 <= subWidth < 9:
                    if not visitList[subHeight][subWidth]:
                        if subHeight == goalHeight and subWidth == goalWidth:
                            result = (thisDeque[2] + 1)
                            resultCheck = True
                            return
                        visitList[subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])


upDown = [-2, -3, -3, -2, 2, 3, 3, 2]
leftRight = [-3, -2, 2, 3, -3, -2, 2, 3]

result = 0
resultCheck = False

visitList = [[False for i in range(9)] for i in range(10)]

startHeight, startWidth = map(int, (input()).split())
goalHeight, goalWidth = map(int, (input()).split())

bfs(startHeight, startWidth, goalHeight, goalWidth, visitList)

if resultCheck:
    print(result)
else:
    print(-1)