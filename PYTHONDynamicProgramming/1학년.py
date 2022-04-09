allNum = int(input())
numList = list(map(int, input().split()))

dp = [[0 for i in range(21)] for i in range(allNum-1)]
dp[0][numList[0]] = 1

for i in range(1, allNum-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            if (j + numList[i]) <= 20 :
                dp[i][j + numList[i]] += dp[i-1][j]

            if (j - numList[i]) >= 0:
                dp[i][j - numList[i]] += dp[i-1][j]

print(dp[allNum-2][numList[allNum-1]])