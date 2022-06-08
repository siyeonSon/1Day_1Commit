#include <bits/stdc++.h>
using namespace std;

int Solve(vector<pair<int, int>> meeting) {
    int answer = 0;
    //end time 을 기준으로 정렬
    sort(meeting.begin(), meeting.end());

    int time = 0;
    for (int i = 0; i < meeting.size(); i++) {
        if (meeting[i].second >= time) {
            time = meeting[i].first;
            answer++;
        }
    }
    
    return answer;
}


int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> meeting(n);
    for (int i = 0; i < n; i++) 
        cin >> meeting[i].second >> meeting[i].first;  //<end time, start time>

    cout << Solve(meeting);

    return 0;
}