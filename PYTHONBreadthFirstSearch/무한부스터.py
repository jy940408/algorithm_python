from collections import deque
import sys

def bfs(heightRoot, widthRoot, visitList):
    global result

    bfsDeque = deque()
    bfsDeque.append([heightRoot, widthRoot, 0])

    while bfsDeque:
        thisDeque = bfsDeque.popleft()
        thisHeight = thisDeque[0]
        thisWidth = thisDeque[1]

        for i in range(2):
            for j in range(1, board[thisHeight][thisWidth]+1):
                subHeight = (thisHeight + (down[i]*j))
                subWidth = (thisWidth + (right[i]*j))

                if 0 <= subHeight < height and 0 <= subWidth < width:
                    if not visitList[subHeight][subWidth]:
                        if subHeight == (height-1) and subWidth == (width-1):
                            result = (thisDeque[2] + 1)
                            return
                        visitList[subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])

result = 0
down = [1,0]
right = [0,1]

height, width = map(int, (sys.stdin.readline()).split())
board = []
visitList = [[False for i in range(width)] for i in range(height)]
for i in range(height):
    board.append(list(map(int, (sys.stdin.readline()).split())))

bfs(0, 0, visitList)

print(result)