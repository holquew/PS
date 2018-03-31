#include <iostream>
using namespace std;

int main(void) {
	int in = 0, out = 0;
	int subtotal = 0, max = 0;
	for (int i = 0; i < 4; i++) { 
		scanf("%d %d", &out, &in); 
		subtotal -= out;
		subtotal += in;
		if (max <= subtotal) max = subtotal;
	}
	cout << max << endl;
}