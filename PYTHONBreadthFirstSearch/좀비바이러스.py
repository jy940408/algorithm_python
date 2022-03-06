from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[[0, 0] for i in range(width)] for i in range(height)]
bfsDeque = deque()

for i in range(height):
    firstLine = input().split()
    for j in range(width):
        board[i][j] = int(firstLine[j])

        if board[i][j] == 1:
            bfsDeque.append([i, j, 1, 0])
            visitList[i][j] = [1, -1]
        elif board[i][j] == 2:
            bfsDeque.append([i, j, 2, 0])
            visitList[i][j] = [2, -1]

result = [0, 1, 1, 0]
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if visitList[thisDeque[0]][thisDeque[1]][0] != 3:
        for i in range(4):
            thisHeight = (thisDeque[0] + upDown[i])
            thisWidth = (thisDeque[1] + leftRight[i])

            if 0 <= thisHeight < height and 0 <= thisWidth < width:
                if board[thisHeight][thisWidth] != -1:
                    if visitList[thisHeight][thisWidth][0] != 3:
                        if visitList[thisHeight][thisWidth][0] == 0:
                            visitList[thisHeight][thisWidth] = [thisDeque[2], (thisDeque[3]+1)]
                            result[thisDeque[2]] += 1
                            bfsDeque.append([thisHeight, thisWidth, thisDeque[2], (thisDeque[3]+1)])

                        else:
                            if thisDeque[2] != visitList[thisHeight][thisWidth][0]:
                                if (thisDeque[3]+1) <= visitList[thisHeight][thisWidth][1]:
                                    result[visitList[thisHeight][thisWidth][0]] -= 1
                                    result[3] += 1
                                    visitList[thisHeight][thisWidth] = [3, (thisDeque[3]+1)]

print(result[1], result[2], result[3])