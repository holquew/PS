#include <stdio.h>
#include <string.h>

int main() {
	char str[13] = " ", temp;
	int i, j, leng, t;

	gets(str);
	leng = strlen(str);

	for (i = 0; i < leng; i++) {
		for (j = 0; j < leng; j++) {
			if (str[i] > str[j]) {
				temp = str[i];
				str[i] = str[j];
				str[j] = temp;
			}
		}
	}
	puts(str);
	return 0;

}