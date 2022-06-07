#include <bits/stdc++.h>
using namespace std;

int Solve(int k, vector<int> vec) {
    int answer = 0;
    for (int i = vec.size()-1; i > -1; i--) {
        if (k / vec[i] != 0) {
            answer += k / vec[i];
            k = k % vec[i];
        }
    }
    return answer;
}


int main() {
    int n, k;
    cin >> n >> k;
    vector<int> vec(n);
    for (int i = 0; i < n; i++) cin >> vec[i];

    cout << Solve(k, vec);

    return 0;
}