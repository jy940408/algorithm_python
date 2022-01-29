import sys
sys.setrecursionlimit(10**6)

def dfs(today, yesterday, list):
    global visitList

    if today == dayNum:
        for i in range(dayNum):
            print(list[i])

        exit()
    
    for i in riceList[today]:
        if not visitList[today][i]:
            if i != yesterday:
                visitList[today][i] = True
                dfs((today+1), i, (list + [i]))

dayNum = int(input())

riceList = []
visitList = [[False for i in range(10)] for i in range(dayNum)]
for i in range(dayNum):
    firstLine = (input()).split()

    riceNum = int(firstLine[0])
    subList = []
    for j in range(1, riceNum+1):
        subList.append(int(firstLine[j]))
    
    riceList.append(subList)

dfs(0, 0, [])

print(-1)