cost = list()
dp = list()

def maxPath(row, col):
    if row == 0 and col == 0:
        return cost[0][0]
    if dp[row][col] != -1:
        return dp[row][col]
    if row != 0 and col != 0:
        dp[row][col] = max(maxPath(row, col - 1), maxPath(row - 1, col)) + cost[row][col]
    elif row == 0:
        dp[row][col] = maxPath(row, col - 1) + cost[row][col]
    else:
        dp[row][col] = maxPath(row - 1, col) + cost[row][col]
    return dp[row][col]

for t in range(int(input())):
    cost.clear()
    dp.clear()
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n*2-1)]
    for i in range(n*2-1):
        dp.append([])
        temp = list()
        for j in range(n*2-1):
            dp[i].append(-1)
            if len(arr) > i:
                if len(arr[i]) > j:
                    temp.append(arr[i][j])
                else:
                    temp.append(0)
            else:
                temp.append(0)
        cost.append(temp)
    print("Case ", str(t+1), ":", maxPath(n*2-2, n*2-2))

# 2
# 4
# 7
# 6 4
# 2 5 10
# 9 8 12 2
# 2 12 7
# 8 2
# 10
# 2
# 1
# 2 3
# 1
