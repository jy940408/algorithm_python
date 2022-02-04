from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, (input()).split())
nowHeight, nowWidth = map(int, (input()).split())
escapeHeight, escapeWidth = map(int, (input()).split())

board = [list(map(int, (input()).split())) for i in range(height)]
visitList = [[[False for i in range(width)] for i in range(height)] for i in range(2)]

bfsDeque = deque()
bfsDeque.append([(nowHeight-1), (nowWidth-1), 0, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == (escapeHeight-1) and thisDeque[1] == (escapeWidth-1):
        result = thisDeque[3]
        break

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if not visitList[thisDeque[2]][subHeight][subWidth]:
                if board[subHeight][subWidth] == 0:
                    visitList[thisDeque[2]][subHeight][subWidth] = True
                    bfsDeque.append([subHeight, subWidth, thisDeque[2], (thisDeque[3]+1)])
                else:
                    if thisDeque[2] == 0:
                        visitList[thisDeque[2]+1][subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1), (thisDeque[3]+1)])

print(result)