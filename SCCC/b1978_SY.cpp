#include <bits/stdc++.h>
using namespace std;

// true -> primenumber, false -> primenumber X
vector<bool> makePrimeNums(int num) {
    //배열초기화
    vector<bool> primeNums;
    primeNums.push_back(false);  //0 is not primenumber
    primeNums.push_back(false);  //1 is not primenumber
    for (int i = 2; i <= num; i++) {
        primeNums.push_back(true);
    }
    //eratos
    for (int i = 2; i <= num; i++) {
        if (primeNums[i]) {
            for (int j = i+i; j <= num; j += i) {
                primeNums[j] = false;
            }
        }
    }
    return primeNums;
}

int main() {
    int n, tmp, answer = 0;
    vector<int> nums;
    vector<bool> primeNums;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        nums.push_back(tmp);
    }

    primeNums = makePrimeNums(*max_element(nums.begin(), nums.end()));
    
    for (int i = 0; i < n; i++) {
        if (primeNums[nums[i]]) 
            answer++; 
    }
    cout << answer;
}