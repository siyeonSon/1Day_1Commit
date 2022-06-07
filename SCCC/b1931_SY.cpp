#include <bits/stdc++.h>
using namespace std;

int Solve(vector<int> vec) {
    int answer = 0;
    vector<bool> check(*max_element(vec.begin(), vec.end()) + 1);
    vector<int> time(vec.size()/2);

    for (int i = 0; i < time.size(); i++) {
        time[i] = vec[2*i+1] - vec[2*i];
        cout << time[i] << " ";
    }
    
    
    
    return answer;
}


int main() {
    int n;
    cin >> n;
    vector<int> vec(n*2);
    for (int i = 0; i < n; i++) 
        cin >> vec[2*i] >> vec[2*i+1];

    cout << Solve(vec);

    return 0;
}