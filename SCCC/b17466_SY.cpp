#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, p;
    long long mid = 1;
    cin >> n >> p;

    for (int i = 1; i <= n; i++)
        mid = (mid * (i % p)) % p;
    cout << mid;

    return 0;
}