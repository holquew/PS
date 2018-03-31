#include <iostream>
#include <queue>
using namespace std;

bool adj[1001][1001] = { 0, };
bool D_visited[1001] = { 0, };
bool B_visited[1001] = { 0, };

void DFS(int cur, int N) {
	cout << cur << ' ';
	D_visited[cur] = true;

	for (int i = 1; i <= N; i++) {
		if (adj[i][cur] && !D_visited[i]) {
			DFS(i, N);
		}
	}
}

void BFS(int cur, int N) {
	queue<int> q;
	B_visited[cur] = true;
	q.push(cur);

	while (!q.empty()) {
		cur = q.front();
		cout << cur << ' ';
		q.pop();
		for (int i = 1; i <= N; i++) {
			if (adj[i][cur] && !B_visited[i]) {
				B_visited[i] = true;
				q.push(i);
			}
		}
	}
}


int main() {

	vector<int> order;

	int vertex = 0, edge = 0;
	int start = 0;
	cin >> vertex >> edge >> start;

	int u, v;
	//牢立 青纺 积己
	for (int i = 0; i < edge; i++) {
		cin >> u >> v;
		adj[u][v] = adj[v][u] = 1;
	}
	DFS(start, vertex);
	cout << endl;
	BFS(start, vertex);
	cout << endl;


	return 0;
}