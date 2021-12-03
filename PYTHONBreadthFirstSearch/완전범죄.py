from queue import Queue

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

        for i in range(2):
            subRoot = 0
            if i == 0:
                subRoot = (thisRoot + moveList[i])
            else:
                subRoot = (thisRoot - moveList[i])

            if 1 <= subRoot < (buildingNum+1):
                if not visitList[subRoot]:
                    if board[subRoot] != 1:
                        visitList[subRoot] = True
                        bfsQueue.put([subRoot, (thisQueue[1]+1)])

result = 0
resultCheck = False

buildingNum, startNum, goalNum, forwardNum, backNum, policeNum = map(int, (input()).split())
moveList = [forwardNum, backNum]
board = [0 for i in range(buildingNum+1)]
visitList = [False for i in range(buildingNum+1)]

if policeNum != 0:
    policeList = (input()).split()
    for i in range(policeNum):
        board[int(policeList[i])] = 1

bfs(startNum, visitList)

if resultCheck:
    print(result)
else:
    print("BUG FOUND")