//미완
#include <bits/stdc++.h>
using namespace std;
char[] lastBulb;  //이어지는 전구의 색깔

int count(char[] nums) {
    int count = 0;
    for(int i = 0; i < nums.size(); i++) {
        if (lastBulb != nums[i]) {
            count++;
            lastBulb = nums[i];
        }
    }
    lastBulb = nums[nums.size()-1];  //마지막 원소
    return count;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    vector<int> resultArr;
    int n;
    char[] tmp;
    vector<char[]> vec;

    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> tmp;
        vec.push_back(tmp);
    }
    
    sort(vec.begin(), vec.end());

    do {
        lastBulb = vec[0][0];
        int sum = 0;
        for (int i = 0; i < vec.size(); i++) {
            sum += count(vec[i]);
        }
        resultArr.push_back(sum);

    } while (next_permutation(vec.begin(), vec.end()));
    
    cout << *min_element(resultArr.begin(), resultArr.end());

    return 0;
}