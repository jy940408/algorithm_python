from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, (input()).split())

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[-1 for i in range(width)] for i in range(height)]

bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = int(firstLine[j])
        if board[i][j] == 1:
            visitList[i][j] = 0
            bfsDeque.append([i, j, 0])

while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if visitList[subHeight][subWidth] == -1:
                visitList[subHeight][subWidth] = (thisDeque[2]+1)
                bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])

for i in range(height):
    result = ""
    for j in range(width):
        result += (str(visitList[i][j])) + " "
    print(result)