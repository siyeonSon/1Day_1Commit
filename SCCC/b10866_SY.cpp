#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, pushNum;
    string com;
    deque<int> deque;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> com;

        if (com == "push_front") {
            cin >> pushNum;
            deque.push_front(pushNum);
        }
        else if (com == "push_back") {
            cin >> pushNum;
            deque.push_back(pushNum);
        }
        else if (com == "pop_front") {
            if (!deque.empty()) {
                cout << deque.front() << "\n";
                deque.pop_front();
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (com == "pop_back") {
            if (!deque.empty()) {
                cout << deque.back() << "\n";
                deque.pop_back();
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (com == "size") {
            cout << deque.size() << "\n";
        }
        else if (com == "empty") {
            cout << deque.empty() << "\n";
        }
        else if (com == "front") {
            if (!deque.empty()) {
                cout << deque.front() << "\n";
            }
            else {
                cout << -1 << "\n";
            }
        }
        else if (com == "back") {
            if (!deque.empty()) {
                cout << deque.back() << "\n";
            }
            else {
                cout << -1 << "\n";
            }
        }
    }

    return 0;
}