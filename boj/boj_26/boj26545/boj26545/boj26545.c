#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int max;
	scanf("%d", &max);
	int sum = 0;
	for (int i = 1; i <= max; i++) {
		int value;
		scanf("%d", &value);
		sum += value;
	}
	printf("%d", sum);
	return 0;
}