memberNum, levelNum = map(int, (input()).split())

levelList = []
for i in range(memberNum):
    levelList.append(int(input()))

levelList = sorted(levelList)

start, mid, last = levelList[0], 0, (levelList[(memberNum-1)]+levelNum)
result = 0
while start <= last:
    
    levelSum = 0
    mid = (start+last)//2

    for i in range(memberNum):
        if levelList[i] >= mid:
            break

        levelSum += (mid - levelList[i])

    if levelSum <= levelNum:
        result = mid
        start = mid + 1
    else:
        last = mid - 1

print(result)