#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k, tmp;
    cin >> n >> k;

    //dp[i]: i원을 만들 경우
    //dp[0]: 0원을 만들 경우 = 동전을 선택하지 않는 경우
    int dp[k+1] = {1};
    int coin[k+1] = {-1};

    for (int i = 0; i < n; i++) {
        cin >> tmp;
        for (int j = 0; j <= k-tmp; j++) {
            dp[j+tmp] += dp[j];
        }
    }

    cout << dp[k];

    return 0;
}