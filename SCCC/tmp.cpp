/**
#include <bits/stdc++.h>
using namespace std;
int lastBulb;  //이어지는 전구의 색깔

int count(vector<int> vec) {
    int count = 0;
    for(int i = 0; i < vec.size(); i++) {
        if (lastBulb != vec[i]) {
            count++;
            lastBulb = vec[i];
        }
    }
    lastBulb = vec.back();  //마지막 원소
    return count;
}

// 2차원 벡터로 만들기 위해 string 형태를 vector<int> 로 변환함
vector<int> StringToVectorInt (string str) {
    vector<int> vec;
    int num;
    stringstream iss(str);
    
    while (iss >> num)
        vec.push_back(num);
        
    return vec;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    vector<int> resultArr;
    int n;
    string tmp;
    vector<vector<int>> vec;

    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> tmp;
        vec.push_back(StringToVectorInt(tmp));
    }
    
    lastBulb = vec[0][0];
    sort(vec.begin(), vec.end());

    do {
        int sum = 0;
        for (int i = 0; i < vec.size(); i++) {
            sum += count(vec[i]);
        }
        resultArr.push_back(sum);

    } while (next_permutation(vec.begin(), vec.end()));
    
    cout << *min_element(resultArr.begin(), resultArr.end());

    return 0;
}
*/
/**
 * 
#include <bits/stdc++.h>
using namespace std;
int main() {
    string str = "123";
    for (int i =0; i<str.size(); i++) {
        if (str[i].compare("1"))
            cout << str[i] << " ";
    }
}
*/

#include <bits/stdc++.h>
using namespace std;
int main() {
    vector<int> v = { 1, 2, 3, 4, 5 };
    cout << accumulate(0, 2, 0);
    return
}