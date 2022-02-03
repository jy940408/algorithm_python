from collections import deque
import sys

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]
knightHeight = [-1, -2, -2, -1, 1, 2, 2, 1]
knightWidth = [-2, -1, 1, 2, -2, -1, 1, 2]

knightNum = int(sys.stdin.readline())
width, height = map(int, (sys.stdin.readline()).split())

board = [list(map(int, (sys.stdin.readline()).split())) for i in range(height)]
visitList = [[[False for i in range(width)] for i in range(height)] for i in range(knightNum+1)]

bfsDeque = deque()
bfsDeque.append([0, 0, 0, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == (height-1) and thisDeque[1] == (width-1):
        result = thisDeque[3]
        break

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if not visitList[thisDeque[2]][subHeight][subWidth]:
                if board[subHeight][subWidth] != 1:
                    visitList[thisDeque[2]][subHeight][subWidth] = True
                    bfsDeque.append([subHeight, subWidth, thisDeque[2], (thisDeque[3]+1)])
    
    if thisDeque[2] < knightNum:
        for i in range(8):
            subHeight = (thisDeque[0] + knightHeight[i])
            subWidth = (thisDeque[1] + knightWidth[i])

            if 0 <= subHeight < height and 0 <= subWidth < width:
                if not visitList[(thisDeque[2]+1)][subHeight][subWidth]:
                    if board[subHeight][subWidth] != 1:
                        visitList[(thisDeque[2]+1)][subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1), (thisDeque[3]+1)])

print(result)