#include <bits/stdc++.h>
using namespace std;

string Solve() {
    string str;
    cin >> str;
    stack<char> stk;
    for (auto i : str) {
        if (i == '(') {
            stk.push(i);
        }
        else {
            if (!stk.empty()) stk.pop();
            else return "NO";
        }
    }
    if (stk.empty()) return "YES";
    else return "NO";
}


int main() {
    int n;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << Solve() << "\n";
    }

    return 0;
}