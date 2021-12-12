from collections import deque

def bfs(firstNum, secondNum):
    bfsDeque = deque()
    bfsDeque.append([firstNum, secondNum, 0])
    check = [-1]*(200)
    while bfsDeque:
        thisDeque = bfsDeque.popleft()
        if thisDeque[0] <= thisDeque[1] and check[thisDeque[0]] == -1:
            bfsDeque.append([thisDeque[0]*2, thisDeque[1]+3, thisDeque[2]+1])
            bfsDeque.append([thisDeque[0]+1, thisDeque[1], thisDeque[2]+1])
            if thisDeque[0] == thisDeque[1]:
                return thisDeque[2]

roundNum = int(input())
for i in range(roundNum):
    firstNum, secondNum = map(int, (input()).split())
    print(bfs(firstNum, secondNum))