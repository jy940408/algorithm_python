import sys
sys.setrecursionlimit(10**5)

def dfsCheck(thisWork, board, resultNum):
    global result, visitList

    for i in board[thisWork]:
        if not visitList[i]:
            visitList[i] = True
            result += 1
            dfsCheck(i, board, (resultNum+1))

workNum, orderNum = map(int, input().split())

board = [[] for i in range(workNum+1)]
visitList = [False for i in range(workNum+1)]
for i in range(orderNum):
    startNum, goalNum = map(int, input().split())
    board[goalNum].append(startNum)

goalWork = int(input())

result = 0
dfsCheck(goalWork, board, 0)
print(result)