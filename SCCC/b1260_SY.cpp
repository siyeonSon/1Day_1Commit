#include <bits/stdc++.h>
using namespace std;


/*
void DFS(bool visited, vector<int> graph, int x) {
    visited[x] = true;  //현재 노트 방문 처리
    cout << x << " ";
    //현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for (int i = 0; i < graph[x].size(); i++) {
        int y = graph[x][i];
        if (!visited[y]) {
            DFS(visited, graph, y);
        }
    }
}

void BFS(bool visited, vector<int> graph, int start) {

    
}

*/



int main() {
    int n, m, v;  //n: 정점의 개수, m: 간선의 개수, v:탐색 시작 정점
    cin >> n >> m >> v;

    bool visited[n+1];
    fill(check, check+n+1, false);
    vector<int> graph[n+1];

    int a, b;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        graph[a].push_back(b);  //그래프 생성 방법: 인접 리스트
    }

    for (int i = 0; i < m; i++) {
        cout << graph[i] << "\n";
    }

    //DFS(visited, graph, 1);
    fill(check, check+n+1, false);
    //BFS(visited, graph, 1);

    return 0;
}