from collections import deque

upDown = [-1, -2, -2, -1, 1, 2, 2, 1]
leftRight = [-2, -1, 1, 2, -2, -1, 1, 2]

start = input()
startHeight, startWidth = (ord(start[0])-96), int(start[1])
goal = input()
goalHeight, goalWidth = (ord(goal[0])-96), int(goal[1])

board = [[False for i in range(9)] for i in range(9)]
board[startHeight][startWidth] = True

bfsDeque = deque()
bfsDeque.append([startHeight, startWidth, 0])
result = 0
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == goalHeight and thisDeque[1] == goalWidth:
        result = thisDeque[2]
        break

    for i in range(8):
        thisHeight = (thisDeque[0] + upDown[i])
        thisWidth = (thisDeque[1] + leftRight[i])

        if 1 <= thisHeight < 9 and 1 <= thisWidth < 9:
            if not board[thisHeight][thisWidth]:
                board[thisHeight][thisWidth] = True
                bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

print(result)