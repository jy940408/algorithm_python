firstLine = list(input())
secondLine = list(input())

board = [[0 for i in range(len(secondLine))] for i in range(len(firstLine))]
result = 0
for i in range(len(firstLine)):
    for j in range(len(secondLine)):
        if firstLine[i] == secondLine[j]:
            board[i][j] += 1
        
        if i != 0 and j != 0:
            board[i][j] += board[i-1][j-1]
            
            if board[i][j] == 0:
                board[i][j] = board[i-1][j]

        elif i != 0 and j == 0:
            if board[i][j] == 0:
                board[i][j] = board[i-1][j]

        if board[i][j-1] > board[i][j]:
            board[i][j] = board[i][j-1]

        if board[i-1][j] > board[i][j]:
            board[i][j] = board[i-1][j] 

        result = max(result, board[i][j])

print(result)