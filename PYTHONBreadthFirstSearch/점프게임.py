from collections import deque

goalNum, jumpNum = map(int, (input()).split())
firstLine = input()
secondLine = input()

board = [[int(i) for i in firstLine], [int(i) for i in secondLine]]

upDown = [1, -1, jumpNum]
leftRight = [0, 0]

bfsDeque = deque()
bfsDeque.append([0, 0, 0])
resultCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(3):
        subHeight, subWidth = 0, 0
        if i == 0 or i == 1:
            subHeight = (thisDeque[0] + leftRight[i])
            subWidth = (thisDeque[1] + upDown[i])
        else:
            if thisDeque[0] == 0:
                subHeight = 1
            else:
                subHeight = 0
            subWidth = (thisDeque[1] + upDown[i])

        if thisDeque[2]+1 <= subWidth < goalNum:
            if board[subHeight][subWidth] == 1:
                board[subHeight][subWidth] = -1
                bfsDeque.append([subHeight, subWidth, (thisDeque[2]+1)])
        elif subWidth >= goalNum:
            resultCheck = True
            break
    if resultCheck:
        break

if resultCheck:
    print(1)
else:
    print(0)