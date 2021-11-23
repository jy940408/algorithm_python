from queue import Queue

def bfs(root):
    global result, visitList, trueCheck

    bfsQueue = Queue()
    bfsQueue.put([root, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        if thisQueue[0] == (allNum-1):
            result = thisQueue[1]
            trueCheck = True
            return

        for i in range(1, board[thisQueue[0]]+1):
            subQueue = (thisQueue[0]+i)
            if subQueue < allNum:
                if not visitList[subQueue]:
                    visitList[subQueue] = True
                    bfsQueue.put([subQueue, thisQueue[1]+1])

result = 0
trueCheck = False
allNum = int(input())
board = [0 for i in range(allNum)]
visitList = [False for i in range(allNum)]
firstLine = (input()).split()
for i in range(allNum):
    board[i] = int(firstLine[i])

bfs(0)

if trueCheck:
    print(result)
else:
    print(-1)