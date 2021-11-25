from queue import Queue
import sys

def bfs(root, visitList):

    bfsQueue = Queue()
    bfsQueue.put([root, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisRoot = thisQueue[0]
        if thisRoot == goalNum:
            print(thisQueue[1])
            return

        for i in range(3):
            subRoot = 0
            if i == 0:
                subRoot = (thisRoot - 1)
            elif i == 1:
                subRoot = (thisRoot + 1)
            else:
                subRoot = thisRoot*2

            if 0 <= subRoot <= 100000:
                if not visitList[subRoot]:
                    visitList[subRoot] = True
                    bfsQueue.put([subRoot, (thisQueue[1]+1)])

input = sys.stdin.readline()

visitList = [False for i in range(100001)]
startNum, goalNum = map(int, (input).split())

bfs(startNum, visitList)
