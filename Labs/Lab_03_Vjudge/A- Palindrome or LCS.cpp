#include<bits/stdc++.h>
using namespace std;

int dp[5005][5005];
string arr;

int rec(int i, int j)
{
    if (j<=i) return 0;
    if (dp[i][j] != -1) return dp[i][j];
    if (arr[i] == arr[j]) return dp[i][j] = rec(i+1, j-1);
    return dp[i][j] = 1 + min(rec(i+1, j), rec(i, j-1));
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    cin >> arr;
    for(int i=0; i<n; i++)
        for (int j=0; j<n; j++)
            dp[i][j] = -1;
    int result = rec(0, n-1);
    printf("%d", result);

}