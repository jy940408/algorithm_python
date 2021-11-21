import sys
from queue import Queue

def bfs(root):
    global visitList, resultList

    bfsQueue = Queue()
    for i in range(len(board[root])):
        bfsQueue.put([board[root][i], 0])
    
    while not bfsQueue.empty():
        thisCity = bfsQueue.get()
        if not visitList[thisCity[0]]:
            visitList[thisCity[0]] = True
            if thisCity[1]+1 == minLen:
                resultList.append(thisCity[0])

            for i in range(len(board[thisCity[0]])):
                if not visitList[board[thisCity[0]][i]]:
                    bfsQueue.put([board[thisCity[0]][i], thisCity[1]+1])
        

cityNum, roadNum, minLen, startCity = map(int, (sys.stdin.readline()).split())
board = [[] for i in range(cityNum+1)]
visitList = [False for i in range(cityNum+1)]
resultList = []

for i in range(roadNum):
    firstCity, secondCity = map(int, (sys.stdin.readline()).split())
    board[firstCity].append(secondCity)

visitList[startCity] = True
bfs(startCity)

resultList.sort()

if len(resultList) != 0:
    for i in range(len(resultList)):
        print(resultList[i])
else:
    print(-1)