def fun(id, msk):
    global a, dp, n, mx
    if msk == mx:
        return 0
    if dp[id][msk] != -1:
        return dp[id][msk]
    ma = 0
    for j in range(n):
        if msk & (1<<j):
            continue
        ma = max(ma, a[id][j] + fun(id+1, (msk|(1<<j))))
    dp[id][msk] = ma
    return ma

while True:
    try:
        t = int(input())
        for tc in range(1, t+1):
            n = int(input())
            mx = (1<<n)-1
            a = [list(map(int, input().split())) for x in range(n)]
            dp = [[-1]*(16) for i in range(65536)]
            print("Case", str(tc), ":", fun(0, 0))
    except:
        pass

# 2
# 2
# 1 5
# 2 1
# 3
# 1 2 3
# 6 5 4
# 8 1 2