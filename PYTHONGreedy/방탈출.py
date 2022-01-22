buttonNum = int(input())
board = list(map(int, (input()).split()))

result = 0
for i in range(buttonNum):
    if board[i] == 1:
        result += 1
        for j in range(3):
            if (i+j) < buttonNum:
                if board[i+j] == 0:
                    board[i+j] = 1
                else:
                    board[i+j] = 0
                
print(result)