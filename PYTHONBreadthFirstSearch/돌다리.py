from queue import Queue
import sys

def bfs(root, visitList):
    global result

    bfsQueue = Queue()
    bfsQueue.put([root, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisRoot = thisQueue[0]

        if thisRoot == goalNum:
            result = thisQueue[1]
            return

        for i in range(6):
            subRoot = (thisRoot + turn[i])
            
            if 0 <= subRoot < 100001:
                if not visitList[subRoot]:
                    visitList[subRoot] = True
                    bfsQueue.put([subRoot, (thisQueue[1]+1)])

            if i == 4 or i == 5:
                multiRoot = (thisRoot*turn[i])

                if 0 <= multiRoot < 100001:
                    if not visitList[multiRoot]:
                        visitList[multiRoot] = True
                        bfsQueue.put([multiRoot, (thisQueue[1]+1)])
            
            

firstNum, secondNum, startNum, goalNum = map(int, (sys.stdin.readline()).split())
visitList = [False for i in range(100001)]

result = 0
turn = [-1, 1, -firstNum, -secondNum, firstNum, secondNum]

bfs(startNum, visitList)

print(result)