from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())

board= [["" for i in range(width)] for i in range(height)]
visitList = [[[[False for i in range(width)] for i in range(height)] for i in range(width)] for i in range(height)]

firstHeight, firstWidth = -1, -1
bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "o":
            if firstHeight == -1:
                firstHeight = i
                firstWidth = j
            else:
                bfsDeque.append([firstHeight, firstWidth, i, j, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        firstHeight = (thisDeque[0] + upDown[i])
        firstWidth = (thisDeque[1] + leftRight[i])
        secondHeight = (thisDeque[2] + upDown[i])
        secondWidth = (thisDeque[3] + leftRight[i])

        if 0 <= firstHeight < height and 0 <= firstWidth < width:
            if board[firstHeight][firstWidth] == "#":
                firstHeight = thisDeque[0]
                firstWidth = thisDeque[1]

        if 0 <= secondHeight < height and 0 <= secondWidth < width:        
            if board[secondHeight][secondWidth] == "#":
                secondHeight = thisDeque[2]
                secondWidth = thisDeque[3]

        if 0 <= firstHeight < height and 0 <= firstWidth < width and 0 <= secondHeight < height and 0 <= secondWidth < width:
            if not visitList[firstHeight][firstWidth][secondHeight][secondWidth]:
                visitList[firstHeight][firstWidth][secondHeight][secondWidth] = True
                bfsDeque.append([firstHeight, firstWidth, secondHeight, secondWidth, (thisDeque[4] + 1)])

        else:
            if 0 > firstHeight or firstHeight >= height or 0 > firstWidth or firstWidth >= width:
                if 0 <= secondHeight < height and 0 <= secondWidth < width:
                    result = (thisDeque[4] + 1)
                    break
            
            elif 0 <= firstHeight < height and 0 <= firstWidth < width:
                if 0 > secondHeight or secondHeight >= height or 0 > secondWidth or secondWidth >= width:
                    result = (thisDeque[4] + 1)
                    break

    if result != -1:
        break

print(result)