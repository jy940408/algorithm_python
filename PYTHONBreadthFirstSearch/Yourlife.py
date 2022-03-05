from collections import deque
import sys

situationNum, changeNum = map(int, (sys.stdin.readline()).split())
board = [[] for i in range(situationNum+1)]
visitList = [False for i in range(situationNum+1)]

for i in range(changeNum):
    startNum, goalNum = map(int, (sys.stdin.readline()).split())
    board[startNum].append(goalNum)

visitList[1] = True
bfsDeque = deque()
bfsDeque.append([1, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    for i in board[thisDeque[0]]:
        if not visitList[i]:
            visitList[i] = True
            bfsDeque.append([i, (thisDeque[1]+1)])

            if i == situationNum:
                result = (thisDeque[1]+1)
                break

    if result != -1:
        break

print(result)