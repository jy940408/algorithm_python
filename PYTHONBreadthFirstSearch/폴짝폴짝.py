from collections import deque

length = int(input())

firstLine = input().split()
board = [0 for i in range(length+1)]
for i in range(1, length+1):
    board[i] = int(firstLine[i-1])

visitList = [False for i in range(length+1)]

startNum, goalNum = map(int, (input()).split())

bfsDeque = deque()
bfsDeque.append([startNum, 0])

result = -1
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == goalNum:
        result = thisDeque[1]
        break

    subCheck = 1
    while (thisDeque[0] + board[thisDeque[0]]*subCheck) < (length+1):
        thisNum = thisDeque[0] + board[thisDeque[0]]*subCheck

        if thisNum < (length+1):
            if not visitList[thisNum]:
                visitList[thisNum] = True
                bfsDeque.append([thisNum, (thisDeque[1] + 1)])
        
        subCheck += 1
    
    subCheck = 1
    while (thisDeque[0] - board[thisDeque[0]]*subCheck) > 0:
        thisNum = thisDeque[0] - board[thisDeque[0]]*subCheck

        if thisNum < (length+1):
            if not visitList[thisNum]:
                visitList[thisNum] = True
                bfsDeque.append([thisNum, (thisDeque[1] + 1)])
        
        subCheck += 1
    
print(result)