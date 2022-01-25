from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())

bfsDeque = deque()
thisPlace = []
board = [["" for i in range(width)] for i in range(height)]
visitList = [[0 for i in range(width)] for j in range(height)]
for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = firstLine[j]

        if board[i][j] == "J":
            thisPlace = [i, j]
        elif board[i][j] == "F":
            bfsDeque.append([i, j, 0, -1])

bfsDeque.append([thisPlace[0], thisPlace[1], 0, 1])

result = 0
resultCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            if board[subHeight][subWidth] != "#":
                if visitList[subHeight][subWidth] == 0:
                    bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1), thisDeque[3]])
                
                elif visitList[subHeight][subWidth] == 1:
                    if thisDeque[3] == -1:
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1), thisDeque[3]])
        else:
            if thisDeque[3] == 1:
                result = (thisDeque[2] + 1)
                resultCheck = True
                break
    
    if resultCheck:
        break

if resultCheck:
    print(result)
else:
    print("IMPOSSIBLE")