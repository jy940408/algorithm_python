from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())

board = [["" for i in range(width)] for i in range(height)]
idxBoard  = [["" for i in range(width)] for i in range(height)]
idxBoard[0][0] = "1 1"
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

bfsDeque = deque()
bfsDeque.append([0, 0])
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == (height-1) and thisDeque[1] == (width-1):
        break

    for i in range(4):
        thisHeight = (thisDeque[0] + upDown[i])
        thisWidth = (thisDeque[1] + leftRight[i])

        if 0 <= thisHeight < height and 0 <= thisWidth < width:
            if board[thisHeight][thisWidth] != "*":
                if idxBoard[thisHeight][thisWidth] == "":
                    idxBoard[thisHeight][thisWidth] = (str(thisDeque[0]+1) + " " + str(thisDeque[1]+1))
                    bfsDeque.append([thisHeight, thisWidth])

thisHeight, thisWidth = (height-1), (width-1)
result = ("\n" + str(height) + " " + str(width))
while True:
    if thisHeight == 0 and thisWidth == 0:
        break

    result = ("\n" + idxBoard[thisHeight][thisWidth] + result)
    
    thisIdx = idxBoard[thisHeight][thisWidth].split()
    thisHeight, thisWidth = int(thisIdx[0])-1, int(thisIdx[1])-1

print(result)