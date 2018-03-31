#include <stdio.h>

int main(void) {
	char input[110];
	while (scanf(" %[^\n]s", input) != EOF) printf("%s\n", input);
	return 0;
}