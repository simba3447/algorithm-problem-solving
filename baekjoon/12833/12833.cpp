#include <iostream>
#include <string>
using namespace std;

int A, B, C;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> A >> B >> C;

    if (C % 2 == 1) {
        A ^= B;
    }
    cout << A << endl;
}