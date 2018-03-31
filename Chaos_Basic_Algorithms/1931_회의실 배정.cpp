#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct {
	int s;	
	int e;	
}time_pair;

bool compare(const time_pair &a, const time_pair &b);

int main (){
	int N;
	int c = 0; //가능한 회의의 개수 카운트
	int temp = -1;
	cin >> N;
	int s, e;
	vector<time_pair> v;
	time_pair t;
	for (int i = 0; i < N; i++) {
		
		scanf("%d %d", &s, &e);
		t.s = s;
		t.e = e;
		v.push_back(t);

	}

	sort(v.begin(), v.end(), compare); //같으면 시작이 빠른 순으로


	
	for (int i = 0; i < N; i++) {
		if (v[i].s >= temp) { 
			temp = v[i].e; 
			c++; 
		}
	}

	cout << c << endl;
	return 0;
}

bool compare(const time_pair &a, const time_pair &b) {
	if (a.e == b.e) return a.s < b.s;
	return a.e < b.e;
}
//변수명을 유니크하게 짓자^^!!