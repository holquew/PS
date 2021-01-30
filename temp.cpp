// #include <iostream>
// using namespace std;

// int main() {
//     int n;
//     cin >> n;
//     if (n % 2 == 0) {
//         cout << "CY"
//              << "\n";
//     } else {
//         cout << "SK" << endl;
//     }
//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int main()
// {

//     // 1부터 4까지 저장할 벡터 선언
//     // 배열도 가능!
//     vector<int> v(4);

//     // 1부터 4까지 벡터에 저장
//     for (int i = 0; i < 4; i++)
//     {
//         v[i] = i + 1;
//     }

//     // next_permutation을 통해서 다음 순열 구하기
//     do
//     {

//         for (int i = 0; i < 4; i++)
//         {
//             cout << v[i] << " ";
//         }

//         cout << '\n';

//     } while (next_permutation(v.begin(), v.end()));

//     for (int i = 0; i < 4; i++)
//     {
//         cout << v[i];
//     }
//     return 0;
// }