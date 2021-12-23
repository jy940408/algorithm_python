from collections import deque

def bfs(goalNum, visitList):
    global result

    bfsDeque = deque()
    bfsDeque.append([1, 0, 0])

    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        for i in range(3):
            display, clipboard = 0, 0
            if i == 0:
                display = thisDeque[0]
                clipboard = thisDeque[0]
            elif i == 1:
                display = (thisDeque[0] + thisDeque[1])
                clipboard = thisDeque[1]
            else:
                display = (thisDeque[0] - 1)
                clipboard = thisDeque[1]
            
            if display == goalNum:
                result = (thisDeque[2] + 1)
                return

            if 0 <= display < 2001 and 0 <= clipboard < 2001:        
                if not visitList[display][clipboard]:
                    visitList[display][clipboard] = True
                    bfsDeque.append([display, clipboard, (thisDeque[2]+1)])
      
result = 0
goalNum = int(input())
visitList = [[False for i in range(2001)] for i in range(2001)]

bfs(goalNum, visitList)

print(result)