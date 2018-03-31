#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int card[500001], question[500001];
//입력 받은거 소팅해서, 소팅한거 그냥 찾으면 됨

bool cmp(const int& first, const int& second) {
	return first < second;
}

int bSearch(int s, int e, int search) {
	int mid;
	if (s > e) return 0;
	mid = (s + e) / 2;
	if (card[mid] == search) return 1;
	else if (card[mid] < search) return bSearch(mid + 1, e, search);
	else return bSearch(s, mid - 1, search);

}

int main(void) {
	cin >> N;
	for (int i = 0; i < N; i++) {
		scanf("%d", &card[i]);
	}
	sort(card, card + N, cmp);
	cin >> M;
	for (int i = 0; i < M; i++) {
		scanf("%d", &question[i]);
		printf("%d ", bSearch(0, N - 1, question[i]));
	}
	cout << endl;
	return 0;
}
