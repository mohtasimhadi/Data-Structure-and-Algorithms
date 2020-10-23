def dfs(x, y):
    global flag, dp, a, b
    if x == 0 and y == 0:
        return
    if flag[x][y] == 0:
        dfs(x-1, y-1)
        print(a[x-1], end='')
    elif flag[x][y] == -1:
        dfs(x, y-1)
        print(b[y-1], end='')
    elif flag[x][y] == 1:
        dfs(x-1, y)
        print(a[x-1], end='')

try:
    while True:
        a, b = map(str, input().split())
        len_a = len(a)
        len_b = len(b)
        flag = [[(0) for i in range(105)] for j in range(105)]
        dp = [[(0) for i in range(105)] for j in range(105)]
        for i in range(len_a+1):
            flag[i][0] = 1
        for i in range(len_b+1):
            flag[0][i] = -1
        for i in range(1, len_a+1):
            for j in range(1, len_b+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    flag[i][j] = 0
                elif dp[i][j-1] >= dp[i-1][j]:
                    dp[i][j] = dp[i][j-1]
                    flag[i][j] = -1
                elif dp[i-1][j] >= dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    flag[i][j] = 1
        dfs(len_a, len_b)
        print()
except:
    pass