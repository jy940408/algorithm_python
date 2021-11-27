from queue import Queue

def bfs(root, visitList):
    global result, resultCheck

    bfsQueue = Queue()
    bfsQueue.put([root, 0])

    while not bfsQueue.empty():
        thisQueue = bfsQueue.get()
        thisRoot = thisQueue[0]

        if thisRoot == goalFloor:
            result = thisQueue[1]
            resultCheck = True
            return

        if 1 <= (thisRoot + upFloor) < (allFloor+1):
            if not visitList[(thisRoot+upFloor)]:
                visitList[(thisRoot+upFloor)] = True
                bfsQueue.put([(thisRoot+upFloor), (thisQueue[1]+1)])

        if 1 <= (thisRoot - downFloor) < (allFloor+1):
            if not visitList[(thisRoot-downFloor)]:
                visitList[(thisRoot-downFloor)] = True
                bfsQueue.put([(thisRoot-downFloor), (thisQueue[1]+1)])

resultCheck = False
result = 0
allFloor, nowFloor, goalFloor, upFloor, downFloor = map(int, (input()).split())
visitList = [False for i in range(allFloor+1)]

bfs(nowFloor, visitList)

if resultCheck:
    print(result)
else:
    print("use the stairs")