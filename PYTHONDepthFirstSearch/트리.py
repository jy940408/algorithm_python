def dfs(root, connectList, visitList, check, delete):
    global result 
        
    visitList[root] = True

    if check == 1:
        if len(connectList[root]) == 0:
            result += 1
        elif len(connectList[root]) == 1 and connectList[root][0] == deleteNode:
            result += 1
    
    for i in connectList[root]:
        if not visitList[i]:
            if check == 1:
                dfs(i, connectList, visitList, 1, deleteNode)
            elif check == 0:
                dfs(i, connectList, visitList, 0, deleteNode)

result = 0;
nodeNum = int(input())
firstLine = input().split()
visitList = [False for i in range(nodeNum)]
connectList = [list() for i in range(nodeNum)]

for i in range(nodeNum):
    node = int(firstLine[i])
    if node != -1:
        connectList[node].append(i)

deleteNode = int(input())

dfs(deleteNode, connectList, visitList, 0, deleteNode)

for i in range(nodeNum):
    if not visitList[i]:
        dfs(i, connectList, visitList, 1, deleteNode)

print(result)
