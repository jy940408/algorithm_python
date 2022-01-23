lessonNum, bluerayNum = map(int, (input()).split())

lessonList = []
start, mid, last, result = 0, 0, 0, 1000000000
firstLine = (input()).split()
for i in range(lessonNum):
    lessonList.append(int(firstLine[i]))

    last += lessonList[i]
    start = max(lessonList[i], start)

while start <= last:

    mid = (start+last)//2

    subResult = 0
    checkNum = 0
    for i in range(lessonNum):

        if checkNum+lessonList[i] > mid:
            checkNum = 0
            subResult += 1
        checkNum += lessonList[i]

    if checkNum != 0:
        subResult += 1

    if subResult > bluerayNum:
        start = mid + 1
    else:
        last = mid - 1
        result = min(result, mid)

print(result)
    
