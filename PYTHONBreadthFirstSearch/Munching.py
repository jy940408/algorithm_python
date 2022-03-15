from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())
board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "B":
            bfsDeque.append([i, j, 0])

result = 0
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        thisHeight = (thisDeque[0] + upDown[i])
        thisWidth = (thisDeque[1] + leftRight[i])

        if 0 <= thisHeight < height and 0 <= thisWidth < width:
            if not visitList[thisHeight][thisWidth]:
                if board[thisHeight][thisWidth] != "*":
                    visitList[thisHeight][thisWidth] = True
                    bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

                    if board[thisHeight][thisWidth] == "C":
                        result = (thisDeque[2]+1)
                        break
    
    if result != 0:
        break

print(result)


