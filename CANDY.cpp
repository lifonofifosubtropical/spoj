// CANDY: Solved by calculating the total sum of
// candy in the bags. When the sum is not divisible
// by the number of bags, it can't be done. Else
// we calculate how much is the difference between
// the amount of candy in the lacking bags and the
// optimal amount (total of candy / number of bags)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	cin >> n;
	while(n != -1)
	{
		vector<int> v;
		int val, prom, cont;
		cont = val = prom = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> val;
			v.push_back(val);
			prom += val;
		}

		if (prom % n != 0)
		{
			cout << -1 << endl;
		}else
		{
			cont = 0;
			sort(v.begin(), v.end());
			for (int i = 0; i < n; ++i)
			{
				if (v[i] > (prom/n))
					break;

				cont += prom/n - v[i];
			}
			cout << cont << endl;
		}
		cin >> n;
	}
	return 0;
}