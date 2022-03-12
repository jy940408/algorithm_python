from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())
leftNum, rightNum = map(int, input().split())

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]
bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = int(firstLine[j])

        if board[i][j] == 2:
            bfsDeque.append([i, j, 0, 0])
            visitList[i][j] = True

result = 1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(2):
        thisHeight = thisDeque[0]
        while True:
            thisHeight += upDown[i]
            if 0 <= thisHeight < height and 0 <= thisDeque[1] < width:
                if not visitList[thisHeight][thisDeque[1]]:
                    if board[thisHeight][thisDeque[1]] != 1:
                        result += 1
                        visitList[thisHeight][thisDeque[1]] = True
                        bfsDeque.append([thisHeight, thisDeque[1], thisDeque[2], thisDeque[3]])
                    else:
                        break
            else:
                break
    
    if thisDeque[2] < leftNum:
        thisWidth = (thisDeque[1] + leftRight[2])

        if 0 <= thisDeque[0] < height and 0 <= thisWidth < width:
            if not visitList[thisDeque[0]][thisWidth]:
                if board[thisDeque[0]][thisWidth] != 1:
                    result += 1
                    visitList[thisDeque[0]][thisWidth] = True
                    bfsDeque.append([thisDeque[0], thisWidth, (thisDeque[2]+1), thisDeque[3]])

    if thisDeque[3] < rightNum:
        thisWidth = (thisDeque[1] + leftRight[3])

        if 0 <= thisDeque[0] < height and 0 <= thisWidth < width:
            if not visitList[thisDeque[0]][thisWidth]:
                if board[thisDeque[0]][thisWidth] != 1:
                    result += 1
                    visitList[thisDeque[0]][thisWidth] = True
                    bfsDeque.append([thisDeque[0], thisWidth, thisDeque[2], (thisDeque[3]+1)])

print(result)