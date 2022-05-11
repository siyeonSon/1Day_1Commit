#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, m;
    vector<int> nums;
    vector<bool> check;
    cin >> n >> m;

    // graph 생성
    for (int i = 1; i <= n; i++)
        nums.push_back(i);

    // check 초기화
    for (int i = 0; i < n; i++) {
        if (i < m)
            check.push_back(true);
        else
            check.push_back(false);
    }

    // next permutation
    do {
        // print
        for (int i = 0; i < nums.size(); i++) { 
            if (check[i])
                cout << nums[i] << " ";
        }
        cout << "\n";
    } while (prev_permutation(check.begin(), check.end()));

    return 0;
}