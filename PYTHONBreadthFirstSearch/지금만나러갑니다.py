from collections import deque

length, firstNum, secondNum = map(int,(input()).split())
board = [[[], []] for i in range(length+1)]

bfsDeque = deque()
bfsDeque.append([0, 0, firstNum])
bfsDeque.append([1, 0, secondNum])
board[firstNum][0].append(0)
board[secondNum][1].append(0)

result = 0
resultCheck = False
while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if (thisDeque[1] + 1) > 20:
        break

    for i in range(2):
        subRoot = 0
        if i == 0:
            subRoot = (thisDeque[2] + 2**(thisDeque[1]))
        else:
            subRoot = (thisDeque[2] - 2**(thisDeque[1]))

        if 1 <= subRoot < (length+1):
            board[subRoot][thisDeque[0]].append((thisDeque[1]+1))
            bfsDeque.append([thisDeque[0], (thisDeque[1]+1), subRoot])

            idx = 0
            if thisDeque[0] == 0:
                idx = 1
            else:
                idx = 0
            
            for i in range(len(board[subRoot][idx])):
                if (thisDeque[1] + 1) == board[subRoot][idx][i]:
                    result = (thisDeque[1] + 1)
                    resultCheck = True
                    break
    
    if resultCheck:
        break

if resultCheck:
    print(result)
else:
    print(-1)