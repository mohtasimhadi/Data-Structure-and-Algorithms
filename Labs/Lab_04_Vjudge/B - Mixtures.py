def sum(start, end):
	global arr
	ans = 0
	for k in range(start, end+1):
		ans = (ans + arr[k]) % 100
	return ans

def rec(i, j):
	global dp, arr
	if i >= j:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]
	dp[i][j] = float('inf')
	for k in range(i, j+1):
		dp[i][j] = min(dp[i][j], rec(i, k)+rec(k+1, j)+sum(i, k)*sum(k+1, j))
	return dp[i][j]

while True:
	try:
		n = int(input())
		arr = list(map(int, input().split()))
		dp = [[-1]*(n+1) for i in range(n+1)]
		print(rec(0, n-1))
	except:
		break