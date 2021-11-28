from collections import deque

result = 0
startNum, goalNum = map(int, (input()).split())
visitList = [False for i in range(100001)]

bfsDeque = deque()
bfsDeque.append([startNum, 0])

while bfsDeque:
    thisQueue = bfsDeque.popleft()
    thisRoot = thisQueue[0]

    if thisRoot == goalNum:
        result = thisQueue[1]
        break

    if 0 <= (thisRoot*2) < 100001:
        if not visitList[(thisRoot*2)]:
            visitList[(thisRoot*2)] = True
            bfsDeque.appendleft([(thisRoot*2), thisQueue[1]])
    if 0 <= (thisRoot+1) < 100001:
        if not visitList[(thisRoot+1)]:
            visitList[(thisRoot+1)] = True
            bfsDeque.append([(thisRoot+1), (thisQueue[1]+1)])
    if 0 <= (thisRoot-1) < 100001:
        if not visitList[(thisRoot-1)]:
            visitList[(thisRoot-1)] = True
            bfsDeque.append([(thisRoot-1), (thisQueue[1]+1)])
    
print(result)