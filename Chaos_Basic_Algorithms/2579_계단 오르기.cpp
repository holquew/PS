#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int stairs[301] = { 0, };
	long long score[301] = { 0, };
	int N;
	int a;
	cin >> N;

	for (int i = 1; i <= N; i++) {
		cin >> a;
		stairs[i] = a;
	}
	score[1] = stairs[1];
	score[2] = score[1] + stairs[2];
	score[3] = std::max(stairs[1], stairs[2]) + stairs[3];
	for (int i = 3; i <= N; i++) {
		score[i] = std::max(score[i - 2], score[i - 3] + stairs[i - 1]) + stairs[i];
	}
	cout << score[N] << endl;
	return 0;
}

