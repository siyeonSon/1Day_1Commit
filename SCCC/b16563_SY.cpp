#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n, tmp, i, max, j;
    vector<int> nums;
    vector<bool> vec;
    vector<int> primenumbers;

    //input
    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> tmp;
        nums.push_back(tmp);
    }

    //find primenumbers
    max = *max_element(nums.begin(), nums.end());
    for (i = 2; i <= max; i++) {
        vec.push_back(true);
    }
    for (i = 2; i <= max; i++) {
        if (vec[i]) {
            for (j = i+i; j <= max; j += i) {
                vec[j] = false;
            }
        }
    }
    for (i = 2; i <= max; i++) {
        if (vec[i]) {
            primenumbers.push_back(i);
        }
    }
    

    //output
    for (i = 0; i < n; i++) {
        j = 0;
        while(nums[i] >= primenumbers[j] * primenumbers[j]) {
        if (nums[i] % primenumbers[j] == 0) {
            cout << primenumbers[j] << " ";
            nums[i] /= primenumbers[j];
        }
        else j++;
        }
        cout << nums[i] << "\n";
    }
    
    return 0;
}