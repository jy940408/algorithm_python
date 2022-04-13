from collections import deque
from operator import truediv

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

roundNum = int(input())

for i in range(roundNum):
    height, width = map(int, input().split())

    board = [["" for i in range(width)] for i in range(height)]
    visitList = [[False for i in range(width)] for i in range(height)]

    bfsDeque = deque()
    for j in range(height):
        firstLine = input()
        for k in range(width):
            board[j][k] = firstLine[k]

            if board[j][k] == "S":
                bfsDeque.append([j, k, 0])

    result = 0
    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        if board[thisDeque[0]][thisDeque[1]] == "G":
            result = thisDeque[2]
            break

        for j in range(4):
            thisHeight = (thisDeque[0] + upDown[j])
            thisWidth = (thisDeque[1] + leftRight[j])

            if 0 <= thisHeight < height and 0 <= thisWidth < width:
                if board[thisHeight][thisWidth] != "X":
                    if not visitList[thisHeight][thisWidth]:
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2] + 1)])
    if result == 0:
        print("No Exit")
    else:
        print("Shortest Path:", result)