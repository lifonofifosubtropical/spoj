/* 
 * SAMER08F: solved by using the sum of
 * squares formula.
 */

#include <stdio.h>

int
main(void)
{
	int n;
	for(scanf("%d", &n); n != 0; scanf("%d", &n)) {
		printf("%d\n", n * (n + 1) * (2*n + 1) / 6);
	}

	return 0;
}
