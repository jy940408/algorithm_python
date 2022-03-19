from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

length = int(input())
board = [list(input()) for i in range(length)]
visitList = [[False for i in range(length)] for i in range(length)]

bfsDeque = deque()
bfsDeque.append([0, 0, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in range(4):
        thisHeight, thisWidth = thisDeque[0], thisDeque[1]
        while True:
            thisHeight += upDown[i]
            thisWidth += leftRight[i]

            if 0 <= thisHeight < length and 0 <= thisWidth < length:
                if not visitList[thisHeight][thisWidth]:
                    if board[thisHeight][thisWidth] == ".":
                        visitList[thisHeight][thisWidth] = True
                        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

                        if thisHeight == (length-1) and thisWidth == (length-1):
                            result = (thisDeque[2]+1)
                            break

                    else: 
                        break  

            else:
                break
        
        if result != -1:
            break
        
    if result != -1:
        break

print(result)