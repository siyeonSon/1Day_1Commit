#include <bits/stdc++.h>
using namespace std;

//최대공약수 -> 유클리드 호제법
int GCD(int a, int b) {
    return b ? GCD(b, (a%b)) : a;
}

//최소공배수 -> a*b == GCD(a,b) * LCM(a,b) 
int LCM(int a, int b) {
  return a * b / GCD(a, b);
}


int main() {
    int n, m;
    cin >> n >> m;
    
    cout << GCD(n,m) << "\n" << LCM(n,m);
    
    return 0;
}