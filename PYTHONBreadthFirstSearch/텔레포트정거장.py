from queue import Queue
import sys

def bfs(root):
    global result

    bfsQueue = Queue()
    bfsQueue.put([root, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisRoot = thisQueue[0]

        if thisRoot == goalNum:
            result = thisQueue[1]
            return
        
        for i in range(len(board[thisRoot])):
            subRoot = board[thisRoot][i]
            if 1 <= subRoot < length+1:
                if not visitList[subRoot]:
                    visitList[subRoot] = True
                    bfsQueue.put([subRoot, (thisQueue[1]+1)])

result = 0 
length, connectNum = map(int, (sys.stdin.readline()).split())
startNum, goalNum = map(int, (sys.stdin.readline()).split())
board = [[(i-1), (i+1)] for i in range(length+1)]
visitList = [False for i in range(length+1)]

for i in range(connectNum):
    firstLine = (sys.stdin.readline()).split()
    board[int(firstLine[0])].append(int(firstLine[1]))
    board[int(firstLine[1])].append(int(firstLine[0]))

bfs(startNum)

print(result)