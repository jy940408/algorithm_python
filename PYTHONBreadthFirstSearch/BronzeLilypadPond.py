from collections import deque

height, width, moveHeight, moveWidth= map(int, (input()).split())
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

upDown = [-moveHeight, -moveHeight, moveHeight, moveHeight, -moveWidth, -moveWidth, moveWidth, moveWidth]
leftRight = [-moveWidth, moveWidth, -moveWidth, moveWidth, -moveHeight, moveHeight, -moveHeight, -moveWidth]

bfsDeque = deque()
goalPlace = []
for i in range(height):
    firstLine = (input()).split()
    for j in range(width):
        board[i][j] = int(firstLine[j])
        if board[i][j] == 3:
            bfsDeque.append([i, j, 0])
            visitList[i][j] = True
        elif board[i][j] == 4:
            goalPlace = [i, j]

result = 0
resultCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(8):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if board[subHeight][subWidth] != 0 and board[subHeight][subWidth] != 2:
                if not visitList[subHeight][subWidth]:
                    visitList[subHeight][subWidth] = True
                    bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])

                    if subHeight == goalPlace[0] and subWidth == goalPlace[1]:
                        result = (thisDeque[2]+1)
                        resultCheck = True
                        break

    if resultCheck:
        break

print(result)