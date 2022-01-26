start, last = map(int,input().split())
 
board = [0]
for i in range(46):
    for j in range(i):
        board.append(i)
 
print(sum(board[start:last+1]))