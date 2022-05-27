#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, pushNum;
    string com;
    vector<int> stack;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> com;

        if (com == "push") {
            cin >> pushNum;
            stack.push_back(pushNum);
        }
        else if (com == "pop") {
            if (!stack.empty()) {
                cout << stack.back() << "\n";
                stack.pop_back();
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (com == "size") {
            cout << stack.size() << "\n";
        }
        else if (com == "empty") {
            cout << stack.empty() << "\n";
        }
        else if (com == "top") {
            if (!stack.empty()) {
                cout << stack.back() << "\n";
            }
            else {
                cout << -1 << "\n";
            }
        }
    }

    return 0;
}