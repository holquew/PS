#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
typedef long long ll;

#define INF 2e9

using namespace std;

ll n, k, l, r, ans;

int main() {
	scanf("%lld%lld", &n, &k);
	l = 1;
	r = n*n;
	ans = 0;
	while (l <= r) {
		long long mid = (l + r) / 2;
		long long cnt = 0;
		for (long long i = 1; i <= n; i++) {   
			ll t = (mid / i);                
			cnt += min(n, t);
		}
		if (cnt >= k) {
			ans = mid;
			r = mid - 1;
		}
		else {
			l = mid + 1;
		}
	}
	printf("%lld\n", ans);
	return 0;

	
}
