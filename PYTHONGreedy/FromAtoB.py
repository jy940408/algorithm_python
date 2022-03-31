import sys

startNum, goalNum = map(int, sys.stdin.readline().split())

result = 0
while startNum != goalNum:
    if startNum > goalNum:
        result += 1

        if startNum%2 == 0:
            startNum //= 2
        else:
            startNum += 1
    else:
        result += (goalNum - startNum)
        break

print(result)