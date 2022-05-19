#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> vec = {0, 0};  //set 0 1
    for (int i = 2; i <= n; i++) {
        vec.push_back(vec[i-1] + 1);
        if (i % 3 == 0) vec[i] = (min(vec[i], vec[i/3] + 1));
        if (i % 2 == 0) vec[i] = (min(vec[i], vec[i/2] + 1));
    }
    cout << vec[n];
    
    return 0;
}