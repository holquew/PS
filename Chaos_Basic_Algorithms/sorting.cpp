#include <iostream>
using namespace std;

int main() {
	int array[10] = { 4,2,7,9,5,1,6,3,0,8 };
	int idx;

	/* insertion sort
	for (int i = 0; i < 10; i++) {
		idx = i;
		for (int j = 0; j < 10 ; j++) {
			if (array[idx] < array[j]) idx = j;
			swap(array[idx], array[i]);
		}

	} */

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10 - i - 1; j++) {
			if (array[j] > array[j + 1]) swap(array[j], array[j + 1]);
		}
	}

	for (int i = 0; i < 10; i++) cout << array[i] << ' ';
	cout << endl;
}