roundNum = int(input())

for i in range(roundNum):
    listNum = int(input())

    board = list(map(int, input().split()))
    board = sorted(board)

    evenList = []
    oddList = []
    for j in range(listNum):
        if j%2 == 0:
            evenList.append(j)
        else:
            oddList.insert(0, j)
    
    resultOrder = (evenList + oddList)
    resultBoard = [0 for i in range(listNum)]
    for j in range(listNum):
        resultBoard[j] = board[resultOrder[j]]

    result = 0
    for j in range(listNum):
        result = max(result, (abs(resultBoard[j%listNum] - resultBoard[(j+1)%listNum])))
    
    print(result)