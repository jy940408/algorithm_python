from collections import deque

roundNum = int(input())

orderList = ["D", "S", "L", "R"]
allResult = ""
for i in range(roundNum):
    startNum, goalNum = map(int, (input()).split())
    visitList = [False for i in range(10000)]
    visitList[startNum] = True
    
    bfsDeque = deque()
    bfsDeque.append([startNum, ""])
    resultCheck = False
    result = ""
    while bfsDeque:
        thisDeque = bfsDeque.popleft()

        for i in range(4):
            subNum = 0

            if orderList[i] == "D":
                subNum = (thisDeque[0]*2)%10000
            elif orderList[i] == "S":
                if thisDeque[0] != 0:
                    subNum = thisDeque[0]-1
                else:
                    subNum = 9999
            elif orderList[i] == "L":
                subNum = (((thisDeque[0]%1000)*10) + thisDeque[0]//1000)
            elif orderList[i] == "R":
                subNum = (((thisDeque[0]%10)*1000) + thisDeque[0]//10)
            
            if not visitList[subNum]:
                if subNum != goalNum:
                    visitList[subNum] = True
                    bfsDeque.append([subNum, thisDeque[1]+orderList[i]])
                else:
                    visitList[subNum] = True
                    resultCheck = True
                    result = thisDeque[1] + orderList[i]
                    break
        
        if resultCheck:
            break

    allResult += result + "\n"

print(allResult)