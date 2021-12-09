from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, (input()).split())
board = [[0 for i in range(width)] for i in range(height)]
resultBoard = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

startHeight = 0
startWidth = 0
for i in range(height):
    firstLine = (input()).split()
    for j in range(width):
        board[i][j] = int(firstLine[j])
        if board[i][j] == 2:
            startHeight = i
            startWidth = j

bfsDeque = deque()
bfsDeque.append([startHeight, startWidth, 0])

while bfsDeque:
    thisDeque = bfsDeque.popleft()
    thisHeight = thisDeque[0]
    thisWidth = thisDeque[1]

    for i in range(4):
        subHeight = (thisHeight + upDown[i])
        subWidth = (thisWidth + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if board[subHeight][subWidth] != 0 and board[subHeight][subWidth] != 2 and not visitList[subHeight][subWidth]:
                visitList[subHeight][subWidth] = True
                resultBoard[subHeight][subWidth] = (thisDeque[2] + 1)
                bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])

for i in range(height):
    result = ""
    for j in range(width):
        if board[i][j] == 1 and resultBoard[i][j] == 0:
            result += "-1 "
        else:
            result += (str(resultBoard[i][j]) + " ")
    print(result)