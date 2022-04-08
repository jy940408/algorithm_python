from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())
board = [["" for i in range(width)] for i in range(height)]
visitList = [[[[False for i in range(width)] for i in range(height)] for i in range(width)] for i in range(height)]

firstHeight, firstWidth = -1, -1
bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "o":
            if firstHeight == -1:
                firstHeight, firstWidth = i, j
            else:
                bfsDeque.append([firstHeight, firstWidth, i, j, 0])
                visitList[firstHeight][firstWidth][i][j] = True

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        firstHeight = (thisDeque[0] + upDown[i])
        firstWidth = (thisDeque[1] + leftRight[i])
        secondHeight = (thisDeque[2] + upDown[i])
        secondWidth = (thisDeque[3] + leftRight[i])

        if 0 <= firstHeight < height and 0 <= firstWidth < width and 0 <= secondHeight < height and 0 <= secondWidth < width:
            if board[firstHeight][firstWidth] == "#":
                firstHeight = thisDeque[0]
                firstWidth = thisDeque[1]

            if board[secondHeight][secondWidth] == "#":
                secondHeight = thisDeque[2]
                secondWidth = thisDeque[3]

            if not visitList[firstHeight][firstWidth][secondHeight][secondWidth]:
                visitList[firstHeight][firstWidth][secondHeight][secondWidth] = True
                bfsDeque.append([firstHeight, firstWidth, secondHeight, secondWidth, (thisDeque[4] + 1)])
        
        else:
            if firstHeight < 0 or firstHeight >= height or firstWidth < 0 or firstWidth >= width:
                if 0 <= secondHeight < height and 0 <= secondWidth < width:
                    result = (thisDeque[4] + 1)
                    break
            
            if secondHeight < 0 or secondHeight >= height or secondWidth < 0 or secondWidth >= width:
                if 0 <= firstHeight < height and 0 <= firstWidth < width:
                    result = (thisDeque[4] + 1)
                    break

    if result != -1:
        break

if result == -1 or result > 10:
    print(-1)
else:
    print(result)