from collections import deque

waterNum, houseNum = map(int, (input()).split())
waterList = list(map(int, (input()).split()))

visitList = {}
bfsDeque = deque()
for i in range(waterNum):
    visitList[waterList[i]] = True
    bfsDeque.append([waterList[i], 0])

leftRight = [-1, 1]

result = 0
thisHouse = 0
while thisHouse != houseNum:
    thisDeque = bfsDeque.popleft()

    for i in range(2):
        subIdx = (thisDeque[0] + leftRight[i])

        if not subIdx in visitList:
            visitList[subIdx] = True
            bfsDeque.append([subIdx, (thisDeque[1]+1)])
            thisHouse += 1

            if thisHouse <= houseNum:
                result += (thisDeque[1] + 1)
            else:
                break
    
    if thisHouse >= houseNum:
        break

print(result)