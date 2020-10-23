x, y = map(int, input().split())
coins = sorted(map(int, input().split()))
dp = [(x+1)*[-1] for i in range(len(coins))]

def coinChange(n, pos):
    if n < 0 or pos < 0:
        return 0
    elif n == 0:
        return 1
    elif dp[pos][n] > -1:
        return dp[pos][n]
    else:
        dp[pos][n] = coinChange(n, pos-1) + coinChange(n-coins[pos], pos)
        return dp[pos][n]

print(coinChange(x, len(coins)-1))