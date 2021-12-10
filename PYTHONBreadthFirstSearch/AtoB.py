from collections import deque

def bfs(startNum):
    global result, resultCheck

    bfsDeque = deque()
    bfsDeque.append([startNum, 0])

    while bfsDeque:
        thisDeque = bfsDeque.popleft()
        
        for i in range(2):
            subNum = 0
            if i == 0:
                subNum = thisDeque[0]*2
            else:
                subNum = (thisDeque[0]*10)+1

            if subNum <= goalNum:
                if subNum == goalNum:
                    result = (thisDeque[1]+2)
                    resultCheck = True
                    return
                bfsDeque.append([subNum, (thisDeque[1]+1)])

result = 0
resultCheck = False

startNum, goalNum = map(int, (input()).split())

bfs(startNum)

if resultCheck:
    print(result)
else:
    print(-1)
