#include <stdio.h>

int main(void)
{
	int t_cases, x, y;
	scanf("%d", &t_cases);

	while(t_cases--) {
		scanf("%d %d", &x, &y);
		if (x == y)
		{
			if (x % 2)
			{
				printf("%d\n", x+x-1);
			} else {
				printf("%d\n", 2*x);
			}
		} else if((x-2)!= y) {
			puts("No Number");
		} else {
			if (x % 2)
			{
				printf("%d\n", x + y -1);
			}else{
				printf("%d\n", x + y);
			}
		}
	}

	return 0;
}
