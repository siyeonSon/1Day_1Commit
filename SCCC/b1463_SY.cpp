#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> count = {0, 0};  //연산 횟수의 최소값
    vector<int> num = {0, 0};  //직전값
    for (int i = 2; i <= n; i++) {
        count.push_back(count[i-1] + 1);
        num.push_back(i-1);
        if (i % 3 == 0 && (count[i] > count[i/3]+1)) {
            count[i] = count[i/3] + 1;
            num[i] = i/3;
        }
        if (i % 2 == 0 && (count[i] > count[i/2]+1)) {
            count[i] = count[i/2] + 1;
            num[i] = i/2;
        }
    }
    
    cout << count[n] << "\n";
    while(n > 0) {
        cout << n << " ";
        n = num[n];
    }
    
    return 0;
}