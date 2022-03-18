height, width = map(int, input().split())

board = [[0 for i in range(width)] for i in range(height)]
for i in range(height):
  firstLine = input()
  for j in range(width):
    board[i][j] = int(firstLine[j])

result = 0
for i in range((height-1), -1, -1):
  for j in range((width-1), -1, -1):
    if board[i][j] == 1:
      result += 1
      for k in range(i+1):
        for l in range(j+1):
          if board[k][l] == 0:
            board[k][l] = 1
          else:
            board[k][l] = 0

print(result)