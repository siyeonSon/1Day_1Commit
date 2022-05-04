#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> vecN;
vector<int> vecM;

//존재하면 1을, 존재하지 않으면 0을 return
int binarySearch(int target, int low, int high)
{
    if (low > high)
        return 0;
    else
    {
        int mid = (low + high) / 2;
        if (vecN[mid] == target)
            return 1;
        else if (target < vecN[mid])
            return binarySearch(target, low, mid - 1);
        else
            return binarySearch(target, mid + 1, high);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); // cin 속도 향상 위해

    int n, m, tmp;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        vecN.push_back(tmp);
    }
    sort(vecN.begin(), vecN.end());

    cin >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> tmp;
        vecM.push_back(tmp);
    }

    for (int i = 0; i < m; i++)
        cout << binarySearch(vecM[i], 0, n - 1) << "\n";

    return 0;
}