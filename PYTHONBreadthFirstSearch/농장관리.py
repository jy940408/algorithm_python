from collections import deque

upDown = [-1, -1, -1, 0, 0, 1, 1, 1]
leftRight = [-1, 0, 1, -1, 1, -1, 0, 1]

height, width = map(int, input().split())

board = [list(map(int, input().split())) for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

result = 0
for i in range(height):
    for j in range(width):
        if board[i][j] > 0 and not visitList[i][j]:
            heightCheck = True

            bfsDeque = deque()
            bfsDeque.append([i, j])

            while bfsDeque:
                thisDeque = bfsDeque.popleft()

                for k in range(8):
                    thisHeight = (thisDeque[0] + upDown[k])
                    thisWidth = (thisDeque[1] + leftRight[k])

                    if 0 <= thisHeight < height and 0 <= thisWidth < width:
                        if board[thisDeque[0]][thisDeque[1]] < board[thisHeight][thisWidth]:
                            heightCheck = False
                        else:
                            if not visitList[thisHeight][thisWidth]:
                                if board[thisDeque[0]][thisDeque[1]] == board[thisHeight][thisWidth]:
                                    visitList[thisHeight][thisWidth] = True
                                    bfsDeque.append([thisHeight, thisWidth])
                    
            if heightCheck:
                result += 1

print(result)