#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    long long n;
    long long q;
    cin >> n;
    q = (long long)sqrt(n);
    if (q * q >= n)
        cout << q;
    else
        cout << q + 1;
    return 0;
}