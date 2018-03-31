#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int Poke_num, Q_num;
int index[100001];
char pokemon[100001][21];

bool cmp(const int &first, const int &second) {
	string F = pokemon[first];
	string S = pokemon[second];
	int size = (F.size() < S.size()) ? F.size() : S.size();

	for (int i = 0; i < size; i++) {
		if (F[i] != S[i])
			//첫 번째가 작으면 이미 정렬 되어 있으니까 true 리턴, 첫 번째가 크면 정렬이 안된 것이니까 false 리턴 (오름차순)
			return F[i] < S[i]; 
	}
	return F.size() < S.size();
}

void binSearch(string name) {
	int start, end, mid;
	start = 1;
	end = 1 + Poke_num;
	string poke;

	while (start <= end) {
		mid = (start + end) / 2;
		poke = pokemon[index[mid]];
		if (poke.compare(name) < 0)
			start = mid + 1;
		else end = mid - 1;
	}
	printf("%d\n", index[end + 1]);
}

int main(void) {
	int i, j;
	char name[21];

	scanf("%d %d", &Poke_num, &Q_num);

	for (i = 1; i <= Poke_num; i++) {
		index[i] = i;
		scanf("%s", pokemon[i]);
	}

	sort(index + 1, index + Poke_num + 1, cmp);
	//cout<< "||||||||||||||||||||||input complete|||||||||||||||||||||"<<endl;

	for (j = 0; j < Q_num; j++) {
		scanf("%s", name);
		string str = name;

		if (name[0] >= '0' && name[0] <= '9') {
			int num = atoi(name);
			cout << pokemon[num] << endl;
		}
		else binSearch(str);
	}
	return 0;
}