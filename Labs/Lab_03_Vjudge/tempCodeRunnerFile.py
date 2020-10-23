def rec(i, j):
    global arr, dp, n
    if j <= i:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if arr[i] == arr[j]:
        dp[i][j] = rec(i+1, j-1)
        return dp[i][j]
    dp[i][j] = 1 + min(rec(i+1, j), rec(i, j-1))
    return dp[i][j]
try:
    n = int(input())
    arr = str(input())
    dp = [[(-1) for j in range(n)] for i in range(n)]
    print(rec(0, n-1))
except:
    pass