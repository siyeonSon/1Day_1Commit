// b2417_SY

#include <iostream>
using namespace std;

int binarySearch(long long low, long long high, long long target)
{
    long long mid = (low + high) / 2;
    if (mid * mid >= target)
    {
        cout << mid << "\n";
        if (mid * mid - target < 1)
            return mid;
        else
            return binarySearch(low, mid - 1, target);
    }
    else
        return binarySearch(mid + 1, high, target);
}

int main()
{
    long long n;
    cin >> n;
    // cout << (long long)ceil(sqrt(n));  -> 부동소수점 오차 때문에 틀림
    cout << binarySearch(1, n / 2, n);
    return 0;
}