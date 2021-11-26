from queue import Queue
import sys

def bfs(root, visitList):
    global result, resultCheck

    bfsQueue = Queue()
    bfsQueue.put([root, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisRoot = thisQueue[0]

        if thisRoot == goalNum:
            result = thisQueue[1]
            resultCheck = True
            return

        for i in range(len(board[thisRoot])):
            subRoot = board[thisRoot][i]

            if 0 <= subRoot < allNum+1:
                if not visitList[subRoot]:
                    visitList[subRoot] = True
                    bfsQueue.put([subRoot, thisQueue[1]+1])

resultCheck = False
result = 0
startNum, goalNum = map(int, (sys.stdin.readline()).split())
allNum, connectNum = map(int, (sys.stdin.readline()).split())

visitList = [False for i in range(allNum+1)]
board = [[] for i in range(allNum+1)]
for i in range(connectNum):
    firstNum, secondNum = map(int, (sys.stdin.readline()).split())
    board[firstNum].append(secondNum)
    board[secondNum].append(firstNum)

bfs(startNum, visitList)

if resultCheck:
    print(result)
else:
    print(-1)