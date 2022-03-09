from collections import deque

firstNum, secondNum, thirdNum = map(int, input().split())
allNum = (firstNum + secondNum + thirdNum)
visitList = [[False for i in range(allNum+1)] for i in range(allNum+1)]

bfsDeque = deque()
bfsDeque.append([firstNum, secondNum, thirdNum])

result = 0
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == thisDeque[1] == thisDeque[2]:
        result = 1
        break

    for i in range(3):
        subDeque = [thisDeque[0], thisDeque[1], thisDeque[2]]
        if thisDeque[i%3] != thisDeque[(i+1)%3]:
            if thisDeque[i%3] > thisDeque[(i+1)%3]:
                subDeque[i%3] -= thisDeque[(i+1)%3]
                subDeque[(i+1)%3] += thisDeque[(i+1)%3]
            else:
                subDeque[i%3] += thisDeque[i%3]
                subDeque[(i+1)%3] -= thisDeque[i%3]

            maxNum = max(subDeque)
            minNum = min(subDeque)

            if not visitList[maxNum][minNum]:
                visitList[maxNum][minNum] = True
                bfsDeque.append([subDeque[0], subDeque[1], subDeque[2]])

print(result)