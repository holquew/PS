#include <iostream>
#include <string>

using namespace std;

bool isHansu(int num)
{
	string str = to_string(num);
	int old = -1, now;

	if (str.length() == 1)
	{
		return true;
	}
	else
	{
		int cnt = 1;
		for (int i = 1; i<  str.length(); i++)
		{
			now = (int)str[i] - (int)str[i - 1];
			if (old == now || i == 1)
				cnt++;
			old = now;
		}

		if (cnt == str.length())
			return true;
	}

	return false;
}
int main()
{
	int N, cnt = 0;

	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		if (isHansu(i))
			cnt++;
	}

	cout << cnt << endl;

	return 0;
}
