#include <bits/stdc++.h>
using namespace std;

int Solve(int m, vector<int> array) {
    int answer = 0;
    int sum = 0;

    for (int i = 0; i < array.size(); i++) {
        for (int j = i; j < array.size(); j++) {
            if (sum < m) {
                sum += array[j];
            }
            else if (sum > m) {
                break;
            }
            if (sum == m) {
                answer++; 
                break; 
            }
            
        }
        sum = 0;
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