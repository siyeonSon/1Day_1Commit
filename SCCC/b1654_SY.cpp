#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, k;
vector<int> vec;

// 만약 만들 수 있으면 해당 숫자를 return 아니면 0 을 return
int accumulate(int lan)
{
    // count
    int count;
    for (auto i = vec.begin(); i != vec.end(); i++)
        count += *i / lan;

    // check
    if (count == k)
        return lan;
    return 0;
}

int main()
{
    int tmp;

    // input
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        vec.push_back(tmp);
    }

    // make sum of vector
    int sum;
    for (auto i = vec.begin(); i != vec.end(); i++)
        sum += *i;

    // sum/k 부터 1씩 줄면서 k개의 랜선을 만들 수 있는지 확인
    for (int i = sum / k; i <= sum / n; i--)
    {
        tmp = accumulate(i);
        if (tmp) // not 0
        {
            cout << tmp;
            break;
        }
        continue;
    }
    return 0;
}