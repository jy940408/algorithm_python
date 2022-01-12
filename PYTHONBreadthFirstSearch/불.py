from collections import deque

roundNum = int(input())

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

result = ""
for i in range(roundNum):
    width, height = map(int, (input()).split())
    board = [["" for i in range(width)] for i in range(height)]
    visitList = [[[-1, -1] for i in range(width)] for i in range(height)]

    person = []
    bfsDeque = deque()
    for j in range(height):
        widthList = input()
        for k in range(width):
            board[j][k] = widthList[k]

            if board[j][k] == "@":
                person = [j, k]
                visitList[j][k][0] = 0
                visitList[j][k][1] = 0
            elif board[j][k] == "*":
                bfsDeque.append([1, j, k, 0])
                visitList[j][k][0] = 1
                visitList[j][k][1] = 0

    bfsDeque.append([0, person[0], person[1], 0])

    resultCheck = False
    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        for j in range(4):
            thisHeight = (thisDeque[1] + upDown[j])
            thisWidth = (thisDeque[2] + leftRight[j])

            if 0 <= thisHeight < height and 0 <= thisWidth < width:
                if visitList[thisHeight][thisWidth][0] == -1 and board[thisHeight][thisWidth] != "#":
                    if thisDeque[0] == 0:
                        visitList[thisHeight][thisWidth][0] = 0
                        visitList[thisHeight][thisWidth][1] = (thisDeque[3]+1)
                        bfsDeque.append([thisDeque[0], thisHeight, thisWidth, (thisDeque[3]+1)])

                    elif thisDeque[0] == 1:
                        visitList[thisHeight][thisWidth][0] = 1
                        visitList[thisHeight][thisWidth][1] = (thisDeque[3]+1)
                        bfsDeque.append([thisDeque[0], thisHeight, thisWidth, (thisDeque[3]+1)])

                elif visitList[thisHeight][thisWidth][0] == 0:
                    if thisDeque[0] == 1:
                        visitList[thisHeight][thisWidth][0] = 1
                        visitList[thisHeight][thisWidth][1] = (thisDeque[3]+1)
                        bfsDeque.append([thisDeque[0], thisHeight, thisWidth, (thisDeque[3]+1)])
            else:
                if thisDeque[0] == 0:
                    result += str((thisDeque[3] + 1)) + "\n"
                    resultCheck = True
                    break

        if resultCheck:
            break

    if not resultCheck:
        result += "IMPOSSIBLE\n"

print(result)