from collections import deque

upDown = [-1, -2, -2, -1, 1, 2, 2, 1]
leftRight = [-2, -1, 1, 2, -2, -1, 1, 2]

width, height = map(int, input().split())

board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "K":
            bfsDeque.append([i, j, 0])

result = 0
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if board[thisDeque[0]][thisDeque[1]] == "H":
        result = thisDeque[2]
        break

    for i in range(8):
        thisHeight = (thisDeque[0] + upDown[i])
        thisWidth = (thisDeque[1] + leftRight[i])

        if 0 <= thisHeight < height and 0 <= thisWidth < width:
            if not visitList[thisHeight][thisWidth]:
                if board[thisHeight][thisWidth] != "*":
                    visitList[thisHeight][thisWidth] = True
                    bfsDeque.append([thisHeight, thisWidth, (thisDeque[2] + 1)])

print(result)