import sys
sys.setrecursionlimit(10**6)

def treeCheck(root, edge, visitList):
    visitList[root] = True
    thisNode = 1

    for i in edge[root]:
        if not visitList[i]:
            thisNode += treeCheck(i, edge, visitList)
    
    nodeNum[root] += thisNode
    
    return nodeNum[root]

node, root, query = map(int, (sys.stdin.readline()).split())
edge = [[] for i in range(node+1)]
nodeNum = [0 for i in range(node+1)]

for i in range(node-1):
    first, second = map(int, (sys.stdin.readline()).split())
    edge[first].append(second)
    edge[second].append(first)

visitList =[False for i in range(node+1)]
treeCheck(root, edge, visitList)

for i in range(query):
    root = int(sys.stdin.readline())
    print(nodeNum[root])