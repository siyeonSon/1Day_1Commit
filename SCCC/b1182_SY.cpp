#include <bits/stdc++.h>
using namespace std;
int answer = 0;
int n, s;
vector<int> vec;

int sum(int a, int b) {
    int sum = 0;
    for (int i = a; i <= b; i++)
        sum += vec[i];
    return sum;
}


int main() {
    int tmp;
    
    cin >> n >> s;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        vec.push_back(tmp);
    } 

    sort(vec.begin(), vec.end());

    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (sum(j, n-1) + vec[i] == 0) {
                answer++;
            }
        }
    }

    cout << answer;

    return 0;
}