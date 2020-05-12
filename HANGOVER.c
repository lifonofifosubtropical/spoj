#include <stdio.h>

int main(void) {
	float addr, min;
	int i;

	scanf("%f", &min);
	while(min != 0.00) {
		i = 3;
		addr = 0.5;
		while(addr <= min){
			addr += (float)1/i;
			i++;
		}
		printf("%d card(s)\n", i-2);
		scanf("%f", &min);
	}

	return 0;
}
