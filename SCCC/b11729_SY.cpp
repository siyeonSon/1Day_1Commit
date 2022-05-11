#include <iostream>
using namespace std;

void move(int begin, int end) {
    cout << begin << " " << end << "\n";
}

void hanoi(int n, int first, int second, int third) {
    if (n == 1) 
        move(first, third);
    else {
        hanoi(n-1, first, third, second);
        move(first, third);
        hanoi(n-1, second, first, third);
    }
}

int main() {
    int n;
    cin >> n;
    cout << (1 << n) - 1 << "\n";  //count
    hanoi(n, 1, 2, 3);
    return 0;
}