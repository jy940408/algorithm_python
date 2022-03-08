from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())

board = [list(map(int, input())) for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

bfsDeque = deque()
bfsDeque.append([0, 0, 0])

result = "IMPOSSIBLE"
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == (height-1) and thisDeque[1] == (width-1):
        result = str(thisDeque[2])
        break

    for i in range(4):
        thisHeight = (thisDeque[0] + (upDown[i]*board[thisDeque[0]][thisDeque[1]]))
        thisWidth = (thisDeque[1] + (leftRight[i]*board[thisDeque[0]][thisDeque[1]]))

        if 0 <= thisHeight < height and 0 <= thisWidth < width:
            if not visitList[thisHeight][thisWidth]:
                visitList[thisHeight][thisWidth] = True
                bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

print(result)
