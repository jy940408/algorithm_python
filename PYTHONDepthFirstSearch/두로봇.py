import sys
sys.setrecursionlimit(10**6)

def dfsCheck(thisRoom, goalRoom, visitList, maxNum, subResult):
    global result

    if thisRoom == goalRoom:
        result = (subResult - maxNum)
        return

    if result != 0:
        return

    for i in board[thisRoom]:
        if not visitList[i[0]]:
            visitList[i[0]] = True
            dfsCheck(i[0], goalRoom, visitList, max(maxNum, i[1]), (subResult+i[1]))
        
roomNum, startNum, goalNum = map(int, input().split())

board = [[] for i in range(roomNum+1)]
visitList = [False for i in range(roomNum+1)]
visitList[startNum] = True

for i in range(roomNum-1):
    firstNum, secondNum, length = map(int, input().split())

    board[firstNum].append([secondNum, length])
    board[secondNum].append([firstNum, length])

result = 0
dfsCheck(startNum, goalNum, visitList, 0, 0)

print(result)