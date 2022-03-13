from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

length = int(input())
board = [list(input()) for i in range(length)]
visitList = [[False for i in range(length)] for i in range(length)]

result = 0
for i in range(length):
    for j in range(length):
        if board[i][j] == "*" and not visitList[i][j]:
            bfsDeque = deque()
            bfsDeque.append([i, j])

            result += 1
            while bfsDeque:
                thisDeque = bfsDeque.popleft()

                for k in range(4):
                    thisHeight = (thisDeque[0] + upDown[k])
                    thisWidth = (thisDeque[1] + leftRight[k])

                    if 0 <= thisHeight < length and 0 <= thisWidth < length:
                        if board[thisHeight][thisWidth] == "*" and not visitList[thisHeight][thisWidth]:
                            visitList[thisHeight][thisWidth] = True
                            bfsDeque.append([thisHeight, thisWidth])

print(result)
                    