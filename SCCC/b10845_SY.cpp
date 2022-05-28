#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, pushNum;
    string com;
    queue<int> queue;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> com;

        if (com == "push") {
            cin >> pushNum;
            queue.push(pushNum);
        }
        else if (com == "pop") {
            if (!queue.empty()) {
                cout << queue.front() << "\n";
                queue.pop();
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (com == "size") {
            cout << queue.size() << "\n";
        }
        else if (com == "empty") {
            cout << queue.empty() << "\n";
        }
        else if (com == "front") {
            if (!queue.empty()) {
                cout << queue.front() << "\n";
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (com == "back") {
            if (!queue.empty()) {
                cout << queue.back() << "\n";
            }
            else {
                cout << -1 << "\n";
            }
        }
    }

    return 0;
}