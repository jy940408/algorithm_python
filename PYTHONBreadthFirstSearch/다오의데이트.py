from collections import deque

upDown = [0, -1, 0, 0, 1]
leftRight = [-1, 0, 0, 1, 0]

height, width = map(int, input().split())

board = [["" for i in range(width)] for i in range(height)]

bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "D":
            bfsDeque.append([i, j, 0, ""])

timeNum = int(input())
moveList = []
for i in range(timeNum):
    secondLine = input().split()
    moveList.append([secondLine[0], secondLine[1]])

result = ""
resultCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[2] < timeNum:
        for i in range(2):
            thisHeight = (thisDeque[0] + upDown[(ord(moveList[thisDeque[2]][i])-65)%7])
            thisWidth = (thisDeque[1] + leftRight[(ord(moveList[thisDeque[2]][i])-65)%7])

            if 0 <= thisHeight < height and 0 <= thisWidth < width:
                if board[thisHeight][thisWidth] != "@":
                    bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1), (thisDeque[3] + moveList[thisDeque[2]][i])])

                    if board[thisHeight][thisWidth] == "Z":
                        resultCheck = True
                        result = (thisDeque[3] + moveList[thisDeque[2]][i])
                        break
    
        if resultCheck:
            break

if resultCheck:
    print("YES\n" + result)
else:
    print("NO")