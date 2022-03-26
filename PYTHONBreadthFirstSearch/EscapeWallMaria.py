from collections import deque
import sys

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

time, height, width = map(int, (sys.stdin.readline()).split())

board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

bfsDeque = deque()
for i in range(height):
    firstLine = (sys.stdin.readline())
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "S":
            bfsDeque.append([i, j, 0])

result = "NOT POSSIBLE"
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == 0 or thisDeque[0] == (height-1) or thisDeque[1] == 0 or thisDeque[1] == (width-1):
        if thisDeque[2] <= time:
            result = str(thisDeque[2])
            break

    for i in range(4):
        thisHeight = (thisDeque[0] + upDown[i])
        thisWidth = (thisDeque[1] + leftRight[i])

        if 0 <= thisHeight < height and 0 <= thisWidth < width:
            if board[thisHeight][thisWidth] != "1":
                if not visitList[thisHeight][thisWidth]:
                    if board[thisHeight][thisWidth] == "D" and i == 0:
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

                    elif board[thisHeight][thisWidth] == "U" and i == 1:
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

                    elif board[thisHeight][thisWidth] == "R" and i == 2:
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

                    elif board[thisHeight][thisWidth] == "L" and i == 3:
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])
                        
                    elif board[thisHeight][thisWidth] == "0":
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

print(result)