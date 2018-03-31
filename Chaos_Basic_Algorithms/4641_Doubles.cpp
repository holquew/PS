#include <iostream>	
using namespace std;

int check(int arr[], int n) {
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i] == 2 * arr[j]) cnt++;
		}
	}
	return cnt;
}

int main(void) {
	int a[15] = { 0, };
	int n = -2, i = 0, num = 0;
	int cnt = 0;
	int b[10] = { 2, 4, 5, 6, 8, };
	
	while (n != -1) {
		cin >> n;
		num++;
		a[i++] = n;
		if (n == 0) {
			--num;
			cnt = check(a, num);
			cout << cnt << endl;
			a[15] = { 0, }; 
			num = 0;
			i = 0;
		}
	}
	return 0;
}