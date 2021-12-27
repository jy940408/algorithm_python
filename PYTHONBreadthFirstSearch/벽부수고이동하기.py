from collections import deque

height, width = map(int, (input()).split())
board = [[0 for i in range(width)] for i in range(height)]
visitList = [[[0, 0] for i in range(width)] for i in range(height)]
visitList[0][0][1] = 1

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

for i in range(height):
    firstLine = input()
    for j in range(width):
        board[i][j] = int(firstLine[j])

bfsDeque = deque()
bfsDeque.append([0, 0, 1, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == (height-1) and thisDeque[1] == (width-1):
        result = visitList[thisDeque[0]][thisDeque[1]][thisDeque[2]]
        break

    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < height and 0 <= subWidth < width:
            
            if board[subHeight][subWidth] == 1 and thisDeque[2] == 1:        
                visitList[subHeight][subWidth][0] = (visitList[thisDeque[0]][thisDeque[1]][1]+1)
                bfsDeque.append([subHeight, subWidth, 0, (thisDeque[3]+1)])
            
            elif board[subHeight][subWidth] == 0 and visitList[subHeight][subWidth][thisDeque[2]] == 0:
                visitList[subHeight][subWidth][thisDeque[2]] = (visitList[thisDeque[0]][thisDeque[1]][thisDeque[2]]+1)
                bfsDeque.append([subHeight, subWidth, thisDeque[2], (thisDeque[3]+1)])

print(result)