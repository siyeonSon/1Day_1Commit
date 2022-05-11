// 풀이 방법 두가지 : 수열 / dfs

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, m;
    vector<int> nums;
    cin >> n >> m;

    // graph 생성
    for (int i = 1; i <= n; i++)
        nums.push_back(i);

    // next permutation
    do
    {
        for (int i = 0; i < m; i++)
            cout << nums[i] << " ";
        cout << "\n";
        reverse(nums.begin() + m, nums.end());
    } while (next_permutation(nums.begin(), nums.end()));

    return 0;
}