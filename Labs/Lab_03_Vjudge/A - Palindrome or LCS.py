def rec(i, j):
    if j <= i:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if arr[i] == arr[j]:
        dp[i][j] = rec(i+1, j-1)
        return dp[i][j]
    dp[i][j] = 1 + min(rec(i+1, j), rec(i, j-1))
    return dp[i][j]
dp = [[-1]*5005]*5005
n = int(input())
arr = str(input())
print(rec(0, n-1))