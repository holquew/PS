#include <cstdio>
#include <algorithm>
using namespace std;

long long N, M;
long long tree[1000001];


int main(void) {
	
	long long logSum;
	long long maxHeight = 0;

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%d", tree + i);
		maxHeight = tree[i] < maxHeight ? maxHeight : tree[i];
	}
	
	long long left = 1; 
	long long right = maxHeight;

	while (left <= right) {
		long long mid = left + right >> 1;
		logSum = 0;
		for (int i = 0; i < N; i++) if (mid < tree[i]) logSum += tree[i] - mid;
		
		if (logSum < M) right = mid - 1;
		else left = mid + 1;
	}
	printf("%d\n", right);

	return 0;

}