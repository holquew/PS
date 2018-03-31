

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, time;
	int sum=0;
	cin >> N;

	vector<int> v;

	for (int i = 0; i < N; i++) {
		cin >> time;
		v.push_back(time);
	}

	sort(v.begin(), v.end()); //결국 정렬해야 함

	for (int i = 0; i < N; i++) {
		sum += (N - i)*v[i];
	}
	cout << sum << endl;
	return 0;
}

