from collections import deque

upDown = [-1, -1, -1, 0, 0, 1, 1, 1]
leftRight = [-1, 0, 1, -1, 1, -1, 0, 1]

width, height = map(int, input().split())

board = [list(input()) for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]
result = 0
for i in range(height):
    for j in range(width):
        if board[i][j] == "." and not visitList[i][j]:
            subResult = 1
            visitList[i][j] = True
            bfsDeque = deque()
            bfsDeque.append([i, j])
            while bfsDeque:
                thisDeque = bfsDeque.popleft()

                for k in range(8):
                    thisHeight = (thisDeque[0] + upDown[k])
                    thisWidth = (thisDeque[1] + leftRight[k])

                    if 0 <= thisHeight < height and 0 <= thisWidth < width:
                        if not visitList[thisHeight][thisWidth]:
                            if board[thisHeight][thisWidth] == ".":
                                visitList[thisHeight][thisWidth] = True
                                subResult += 1
                                bfsDeque.append([thisHeight, thisWidth])
            
            result = max(subResult, result)

print(result)