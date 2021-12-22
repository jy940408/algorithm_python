from collections import deque

length, virusNum = map(int, (input()).split())
board = [[[0, 0] for i in range(length)] for i in range(length)]

virusList = [[] for i in range(virusNum+1)]

for i in range(length):
    firstLine = (input()).split()
    for j in range(length):
        board[i][j][0] = int(firstLine[j])
        if board[i][j][0] != 0:
            virusList[board[i][j][0]].append([i, j])

goalTime, goalHeight, goalWidth = map(int, (input()).split())

bfsDeque = deque()
for i in range(1, virusNum+1):
    if len(virusList[i]) != 0:
        for j in range(len(virusList[i])):
            bfsDeque.append([virusList[i][j][0], virusList[i][j][1], i, 0])

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]


while bfsDeque:
    thisDeque = bfsDeque.popleft()
    
    for i in range(4):
        subHeight = (thisDeque[0] + upDown[i])
        subWidth = (thisDeque[1] + leftRight[i])

        if 0 <= subHeight < length and 0 <= subWidth < length:
            if board[subHeight][subWidth][0] == 0:
                board[subHeight][subWidth][0] = thisDeque[2]
                board[subHeight][subWidth][1] = (thisDeque[3]+1)
                
                bfsDeque.append([subHeight, subWidth, thisDeque[2], (thisDeque[3]+1)])

if board[goalHeight-1][goalWidth-1][1] <= goalTime:
    print(board[goalHeight-1][goalWidth-1][0])
else:
    print(0)