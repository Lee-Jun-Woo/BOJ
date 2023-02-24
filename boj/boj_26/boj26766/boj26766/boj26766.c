#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int howManyHearts;
	scanf("%d", &howManyHearts);
	while (howManyHearts > 0) {
		printf(" @@@   @@@ \n@   @ @   @\n@    @    @\n@         @\n @       @ \n  @     @  \n   @   @   \n    @ @    \n     @     \n");
		howManyHearts--;
	}
	return 0;
}