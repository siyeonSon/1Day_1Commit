#include <bits/stdc++.h>
using namespace std;

int Solve(int m, vector<int> array) {
    int answer = 0;
    queue<int> que;

    for (int i = 0; i < array.size(); i++) {
        for (int j = i+1; j < array.size(); j++) {

        }
    }
    return answer;
}


int main() {
    int n, m, tmp;
    vector<int> array;
    
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        array.push_back(tmp);
    }

    cout << Solve(m, array);

    return 0;
}