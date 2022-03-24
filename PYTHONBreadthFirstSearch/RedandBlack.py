from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

firstLine = ""
while firstLine != "0 0":
    firstLine = input()
    if firstLine != "0 0":
        width, height = map(int, firstLine.split())
        
        board = [["" for i in range(width)] for i in range(height)]
        visitList = [[False for i in range(width)] for i in range(height)]

        bfsDeque = deque()
        for i in range(height):
            secondLine = input()
            for j in range(width):
                board[i][j] = secondLine[j]

                if board[i][j] == "@":
                    bfsDeque.append([i, j])

        result = 1
        while bfsDeque:
            thisDeque = bfsDeque.popleft()

            for i in range(4):
                thisHeight = (thisDeque[0] + upDown[i])
                thisWidth = (thisDeque[1] + leftRight[i])

                if 0 <= thisHeight < height and 0 <= thisWidth < width:
                    if board[thisHeight][thisWidth] == ".":
                        if not visitList[thisHeight][thisWidth]:
                            visitList[thisHeight][thisWidth] = True
                            result += 1
                            bfsDeque.append([thisHeight, thisWidth])

        print(result)

    else:
        break