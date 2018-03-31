#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int dwarf[9];
	int tempi, tempj;
	int sum = 0;
	bool flag = false;
	for (int i = 0; i < 9; i++) {
		cin >> dwarf[i];
	}

	for (int i = 0; i < 9; i++) {
		tempi = dwarf[i];
		dwarf[i] = 0;
		for (int j = 0; j < 9; j++) {
			if (i == j) continue;
			tempj = dwarf[j];
			dwarf[j] = 0;

			for (int i = 0; i < 9; i++) {
				sum += dwarf[i];
			}
			if (sum == 100) { 
				flag = true;
				break; 
			}
			else {
				dwarf[j] = tempj;
				sum = 0;
			}
			if (j == 8) dwarf[i] = tempi;
		}
		if (flag) break;
	}
	sort(dwarf, dwarf+9);
	for (int i = 0; i < 9; i++) {
		if (dwarf[i] == 0) continue;
		cout << dwarf[i] << endl;
	}
	return 0;
}