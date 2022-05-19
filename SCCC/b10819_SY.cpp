#include <bits/stdc++.h>
using namespace std;

int calculate(vector<int> vec) {
    int sum = 0;
    for (int i =0; i < vec.size()-1; i++) {
        sum += abs(vec[i]-vec[i+1]);
    }
    return sum;
}

int main() {
    int n, tmp;
    vector<int> vec;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        vec.push_back(tmp);
    }
    sort(vec.begin(), vec.end());

    vector<int> resultArr;
    do {

        resultArr.push_back(calculate(vec));

    } while (next_permutation(vec.begin(), vec.end()));

    cout << *max_element(resultArr.begin(), resultArr.end());
}