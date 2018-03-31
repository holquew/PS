#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, K;
	vector<int> coin;
	scanf("%d %d", &N, &K);

	for (int i = 0; i < N; i++) {
		int c;
		cin >> c;
		coin.push_back(c);
	}

	int count=0;
	for (int i = N - 1; i >= 0; i--) {
		while (coin[i] <= K) {
			count++;
			K -= coin[i];
		}
	}
	cout << count << endl;

	return 0;
}