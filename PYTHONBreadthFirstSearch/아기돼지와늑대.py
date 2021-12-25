from collections import deque

def boardCheck(subHeight, subWidth, direction, board):
    if direction == 0:
        thisHeight = subHeight
        while board[thisHeight][subWidth] != "." or board[thisHeight][subWidth] != "#":
            thisHeight -= 1
            if board[thisHeight][subWidth] == ".":
                return [thisHeight, subWidth, 0]
            elif board[thisHeight][subWidth] == "#":
                return [(thisHeight+1), subWidth, 1]
    elif direction == 1:
        thisHeight = subHeight
        while board[thisHeight][subWidth] != "." or board[thisHeight][subWidth] != "#":
            thisHeight += 1
            if board[thisHeight][subWidth] == ".":
                return [thisHeight, subWidth, 0]
            elif board[thisHeight][subWidth] == "#":
                return [(thisHeight-1), subWidth, 1]
    elif direction == 2:
        thisWidth = subWidth
        while board[subHeight][thisWidth] != "." or board[subHeight][thisWidth] != "#":
            thisWidth -= 1
            if board[subHeight][thisWidth] == ".":
                return [subHeight, thisWidth, 0]
            elif board[subHeight][thisWidth] == "#":
                return [subHeight, (thisWidth+1), 1]
    elif direction == 3:
        thisWidth = subWidth
        while board[subHeight][thisWidth] != "." or board[subHeight][thisWidth] != "#":
            thisWidth += 1
            if board[subHeight][thisWidth] == ".":
                return [subHeight, thisWidth, 0]
            elif board[subHeight][thisWidth] == "#":
                return [subHeight, (thisWidth-1), 1]

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, (input()).split())

board = [["" for i in range(width)] for i in range(height)]
visitList = [[[] for i in range(width)] for i in range(height)]

bfsDeque = deque()
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]
        if board[i][j] == "W":
            bfsDeque.append([i, j, 0])
            visitList[i][j] = [True]
        elif board[i][j] == "+":
            visitList[i][j] = [False, False, False, False]
        elif board[i][j] == ".":
            visitList[i][j] = [False]

while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            print(subHeight, subWidth, board[subHeight][subWidth])

            if board[subHeight][subWidth] == ".":
                if not visitList[subHeight][subWidth][0]:
                    visitList[subHeight][subWidth][0] = True
                    bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])
            elif board[subHeight][subWidth] == "+":


                if not visitList[subHeight][subWidth][i]:
                    result = boardCheck(subHeight, subWidth, i, board)
                    visitList[subHeight][subWidth][i] = True
                    
                    print("result:", result, subHeight, subWidth, i, visitList[result[0]][result[1]], board[result[0]][result[1]])

                    if board[result[0]][result[1]] == ".":
                        if not visitList[result[0]][result[1]][0]:
                            visitList[result[0]][result[1]][0] = True
                            bfsDeque.append([result[0], result[1], (thisDeque[2]+1)])
                    elif board[result[0]][result[1]] == "+":
                        bfsDeque.append([result[0], result[1], (thisDeque[2]+1)])

print()

for i in range(height):
    result = ""
    for j in range(width):
        if board[i][j] == ".":
            if not visitList[i][j][0]:
                board[i][j] = "P"
        result += board[i][j]
    print(result)