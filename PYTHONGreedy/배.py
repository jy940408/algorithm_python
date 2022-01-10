import sys

crainNum = int(sys.stdin.readline())
crainList = sorted(list(map(int, (sys.stdin.readline()).split())), reverse=True)

boxNum = int(sys.stdin.readline())
boxList = sorted(list(map(int, (sys.stdin.readline()).split())), reverse=True)

if crainList[0] < boxList[0]:
    print(-1)
    sys.exit()
else:
    result = 0
    while True:
        for i in range(len(crainList)):
            if not boxList:
                break
            elif crainList[i] < boxList[-1]:
                break
            else:
                for j in range(len(boxList)):
                    if crainList[i] >= boxList[j]:
                        boxList.pop(j)
                        break
        result += 1
    print(result)