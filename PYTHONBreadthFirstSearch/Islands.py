from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())

board = [list(input()) for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

result = 0
for i in range(height):
    for j in range(width):
        if board[i][j] == "C" or board[i][j] == "L":
            if not visitList[i][j]:
                visitList[i][j] = True
                bfsDeque = deque()
                bfsDeque.append([i, j])

                lCheck = False
                if board[i][j] == "L":
                    lCheck = True

                while bfsDeque:
                    thisDeque = bfsDeque.popleft()

                    for k in range(4):
                        thisHeight = (thisDeque[0] + upDown[k])
                        thisWidth = (thisDeque[1] + leftRight[k])

                        if 0 <= thisHeight < height and 0 <= thisWidth < width:
                            if board[thisHeight][thisWidth] == "C" or board[thisHeight][thisWidth] == "L":
                                if not visitList[thisHeight][thisWidth]:
                                    visitList[thisHeight][thisWidth] = True

                                    if board[thisHeight][thisWidth] == "L":
                                        lCheck = True

                                    bfsDeque.append([thisHeight, thisWidth])

                if lCheck:
                    result += 1

print(result)