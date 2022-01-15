from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, (input()).split())
board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

bfsDeque = deque()
hedgehog = []
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "*":
            bfsDeque.append([i, j, 0, 0])
        elif board[i][j] == "S":
            hedgehog = [i, j]

bfsDeque.append([hedgehog[0], hedgehog[1], 1, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if not visitList[subHeight][subWidth]:
                if thisDeque[2] == 0:
                    if board[subHeight][subWidth] == ".":
                        board[subHeight][subWidth] = "*"
                        visitList[subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, 0, (thisDeque[3] + 1)])

                elif thisDeque[2] == 1:
                    if board[subHeight][subWidth] == ".":
                        visitList[subHeight][subWidth] = True
                        bfsDeque.append([subHeight, subWidth, 1, (thisDeque[3] + 1)])
                    
                    elif board[subHeight][subWidth] == "D":
                        result = (thisDeque[3] + 1)
                        break
    
    if result != -1:
        break

if result == -1:
    print("KAKTUS")
else:
    print(result)