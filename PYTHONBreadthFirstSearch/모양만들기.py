from collections import deque
import sys

upDown = [-1, 1, 0, 0, 0]
leftRight = [0, 0, -1, 1, 0]

height, width = map(int, (sys.stdin.readline()).split())

board = [list(map(int, (sys.stdin.readline()).split())) for i in range(height)]
visitList = set()
result = 0
numBoard = [1]
numIdx = 1

for i in range(height):
    for j in range(width):
        if board[i][j] == 1:
            subResult = 0
            bfsDeque = deque()
            bfsDeque.append([i, j])

            while bfsDeque:
                thisDeque = bfsDeque.popleft()

                for k in range(5):
                    thisHeight = (thisDeque[0] + upDown[k])
                    thisWidth = (thisDeque[1] + leftRight[k])

                    if 0 <= thisHeight < height and 0 <= thisWidth < width:
                        if board[thisHeight][thisWidth] == 1:
                            if not (str(thisHeight) + " " + str(thisWidth)) in visitList:
                                visitList.add((str(thisHeight) + " " + str(thisWidth)))
                                board[thisHeight][thisWidth] = numIdx
                                subResult += 1
                                bfsDeque.append([thisHeight, thisWidth])
            
            numBoard.append(subResult)
            result = max(result, subResult)
            numIdx += 1

for i in range(height):
    for j in range(width):
        if board[i][j] == 0:
            subResult = 0
            visitList = set()
            for k in range(5):
                thisHeight = (i + upDown[k])
                thisWidth = (j + leftRight[k])

                if 0 <= thisHeight < height and 0 <= thisWidth < width:
                    if not (board[thisHeight][thisWidth]) in visitList:
                        visitList.add(board[thisHeight][thisWidth])
                        subResult += (numBoard[board[thisHeight][thisWidth]])
            
            result = max(subResult, result)

print(result)