//분할정복법(Divide And conquer)
//정확히 이해X
#include <bits/stdc++.h>
using namespace std;

long long Pow(long long a, long long b, long long c) {
    long long res = 1;
    while (b > 0) {
        if (b % 2 == 1) res = res * a % c;
        b /= 2;
        a = a * a % c;
    }
    return res;
}


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int a, b, c;
    long long tmp = 1;
    cin >> a >> b >> c;
    cout << Pow(a, b, c);
    return 0;
}