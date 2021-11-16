def dfs(root, goal, board, visitList, lengthDict):
    global result, subResult

    visitList[root] = True

    for i in board[root]:
        if not visitList[i]:
            if lengthDict.get(str(i) + " " + str(root)) != None:
                subResult += lengthDict.get(str(i) + " " + str(root))
            elif lengthDict.get(str(root) + " " + str(i)) != None:
                subResult += lengthDict.get(str(root) + " " + str(i))

            if i == goal:
                result = subResult
            
            dfs(i, goal, board, visitList, lengthDict)

            if lengthDict.get(str(i) + " " + str(root)) != None:
                subResult -= lengthDict.get(str(i) + " " + str(root))
            elif lengthDict.get(str(root) + " " + str(i)) != None:
                subResult -= lengthDict.get(str(root) + " " + str(i))

result = 0
subResult = 0

nodeNum, roundNum = map(int, (input()).split())
board = [[] for i in range(nodeNum+1)]
visitList = [False for i in range(nodeNum+1)]
lengthDict = dict()
for i in range(nodeNum-1):
    firstNode, secondNode, length = map(int, (input().split()))
    board[firstNode].append(secondNode)
    board[secondNode].append(firstNode)
    lengthDict[str(firstNode) + " " + str(secondNode)] = length

for i in range(roundNum):
    visitList = [False for i in range(nodeNum + 1)]
    result = subResult = 0
    start, goal = map(int, (input()).split())
    dfs(start, goal, board, visitList, lengthDict)
    print(result)