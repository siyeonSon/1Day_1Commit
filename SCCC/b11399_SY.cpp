/**
 * 시간 = p1 * 5 + p2 * 4 + p3 * 3 + p4 * 2 + p5 * 1
 * 1 2 3 4 5 처럼 오름차순으로 배열될 때가 최소 시간을 가짐
 * */

#include <bits/stdc++.h>
using namespace std;

int Solve(int n, vector<int> Pi) {
    int answer = 0;
    
    sort(Pi.begin(), Pi.end());
    for (int i = 0; i < Pi.size(); i++) 
        answer += Pi[i] * n--;

    return answer;
}


int main() {
    int n;
    cin >> n;
    vector<int> Pi(n);
    for (int i = 0; i < n; i++) 
        cin >> Pi[i];

    cout << Solve(n, Pi);

    return 0;
}
