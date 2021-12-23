from collections import deque

def bfs():
    global result

    bfsDeque = deque()
    bfsDeque.append([1, 0])

    while bfsDeque:
        thisDeque = bfsDeque.popleft()
        
        for i in range(6):
            subRoot = (thisDeque[0] + diceNum[i])

            if 1 <= subRoot < 101:
                if subRoot == 100:
                    result = (thisDeque[1]+1)
                    return
                if visitList[subRoot] != -1:
                    if visitList[subRoot] != 0:
                        bfsDeque.append([visitList[subRoot], (thisDeque[1]+1)])
                        visitList[visitList[subRoot]] = -1
                        visitList[subRoot] = -1
                    else:
                        visitList[subRoot] = -1
                        bfsDeque.append([subRoot, (thisDeque[1]+1)])
                    

result = 0
diceNum = [1, 2, 3, 4, 5, 6]

ladderNum, snakeNum = map(int, (input()).split())
visitList = [0 for i in range(101)]

ladderList = []
snakeList = []
for i in range(ladderNum):
    firstNum, secondNum = map(int, (input()).split())
    visitList[firstNum] = secondNum
for i in range(snakeNum):
    firstNum, secondNum = map(int, (input()).split())
    visitList[firstNum] = secondNum

bfs()

print(result)