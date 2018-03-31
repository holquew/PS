#include <iostream>
using namespace std;

int f(int x, int y) {
	int s = 0;
	for (; x; x /= y) s += x%y;
	return s;
}

int main(void) {
	for (int i = 1000; i < 10000; i++) {
		if (f(i, 10) == f(i, 12) && f(i, 12) == f(i, 16)) cout << i << endl;
	}
	return 0;
}