#include <bits/stdc++.h>
using namespace std;
vector<int> primenumber;
vector<bool> vec;

//print vector<int> primenumber
void pprint(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";
    cout << "\n\n";
}

//print vector<bool> vec
void vprint(vector<bool> arr) {
    for (int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";
    cout << "\n\n";
}


//true -> primenumber, false -> primenumber X 
void eratos(int start, int end) {
    //Initializing
    for (int i = start; i <= end; i++) {
        vec.push_back(true);
    }

    //eratos
    for (int i = 2; i <= end; i++) {
        if (vec[i]) {
            for (int j = i+i; j <= end; j += i) {
                vec[j] = false;
            }
        }
    }

    //return vector<int>
    for (int i = start; i <= end; i++) {
        if (vec[i]) {
            primenumber.push_back(i);
        }
    }
}

int main() {
    int n;
    cin >> n;

    vec.push_back(false);  //0 is not primenumber
    vec.push_back(false);  //1 is not primenumber
    
    //get primenumber
    int start = 2, end = n;
    while(1) {
        eratos(start, end);
        if (primenumber.size() >= n) break;
        start = end + 1;
        end = end + end;
    }

    cout << primenumber[n-1];
}