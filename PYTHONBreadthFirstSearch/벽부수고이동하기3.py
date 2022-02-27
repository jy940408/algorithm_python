from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width, crashNum = map(int, input().split())

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[[False for i in range(width)] for i in range(height)] for i in range(crashNum+1)]
visitList[0][0][0] = True
for i in range(height):
    firstLine= input()
    for j in range(width):
        board[i][j] = int(firstLine[j])

bfsDeque = deque()
bfsDeque.append([0, 0, 1, 0, 1])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        thisHeight = (thisDeque[0] + upDown[i])
        thisWidth = (thisDeque[1] + leftRight[i])

        if 0 <= thisHeight < height and 0 <= thisWidth < width:
            if board[thisHeight][thisWidth] == 0:
                if not visitList[thisDeque[3]][thisHeight][thisWidth]:
                    visitList[thisDeque[3]][thisHeight][thisWidth] = True
                    bfsDeque.append([thisHeight, thisWidth, (-1*thisDeque[2]), thisDeque[3], (thisDeque[4]+1)])

                    if thisHeight == (height-1) and thisWidth == (width-1):
                        result = (thisDeque[4] + 1)
                        break

            else:
                if thisDeque[3] < crashNum:
                    if not visitList[thisDeque[3]+1][thisHeight][thisWidth]:
                        if thisDeque[2] == 1:
                            visitList[thisDeque[3]+1][thisHeight][thisWidth] = True
                            bfsDeque.append([thisHeight, thisWidth, (-1*thisDeque[2]), (thisDeque[3]+1), (thisDeque[4]+1)])

                        else:
                            bfsDeque.append([thisDeque[0], thisDeque[1], (-1*thisDeque[2]), thisDeque[3], (thisDeque[4]+1)])

    if result != -1:
        break
if height == 1 and width == 1 and board[0][0] == 0:
    print(1)
else:
    print(result)
