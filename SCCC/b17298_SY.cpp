#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    stack<int> st;
    vector<int> answer(v.size(), -1);
    for (int i = 0; i < v.size(); i++) {
        while (!st.empty() && v[st.top()] < v[i]) {
                answer[st.top()] = v[i];
                st.pop();
        }
        st.push(i);
    }

    for (int x : answer) 
        cout << x << " ";

    return 0;
}