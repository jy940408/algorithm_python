from collections import deque

upDown = [0, -1, 1, 0, 0, -1, -1, 1, 1]
leftRight = [0, 0, 0, -1, 1, -1, 1, -1, 1]

board = [["" for i in range(8)] for i in range(8)]
visitList = [[0 for i in range(8)] for i in range(8)]

for i in range(8):
    firstLine = input()
    for j in range(8):
        board[i][j] = firstLine[j]

bfsDeque = deque()
bfsDeque.append([7, 0, 0])

result = 0
resultCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(9):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < 8 and 0 <= subWidth < 8:
            if (subHeight-thisDeque[2]) < 0:
                result = 1
                resultCheck = True
                break

            if visitList[subHeight][subWidth] < (thisDeque[2]+1):
                if board[subHeight-(thisDeque[2])][subWidth] == ".":
                    if board[subHeight-(thisDeque[2]+1)][subWidth] == ".":
                        visitList[subHeight][subWidth] = (thisDeque[2]+1)
                        bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])

    if resultCheck:
        break

print(result)

