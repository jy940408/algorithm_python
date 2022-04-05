from collections import deque

upDown = [-1, -1, -1, 0, 0, 1, 1, 1]
leftRight = [-1, 0, 1, -1, 1, -1, 0, 1]

height, width = map(int, input().split())

board = [list(input()) for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

result = 0
for i in range(height):
    for j in range(width):
        if board[i][j] == "#" and not visitList[i][j]:
            result += 1

            bfsDeque = deque()
            bfsDeque.append([i, j])
            visitList[i][j] = True

            while bfsDeque:
                thisDeque = bfsDeque.popleft()

                for k in range(8):
                    thisHeight = (thisDeque[0] + upDown[k])
                    thisWidth = (thisDeque[1] + leftRight[k])

                    if 0 <= thisHeight < height and 0 <= thisWidth < width:
                        if board[thisHeight][thisWidth] == "#":
                            if not visitList[thisHeight][thisWidth]:
                                visitList[thisHeight][thisWidth] = True
                                bfsDeque.append([thisHeight, thisWidth])

print(result)