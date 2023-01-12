#include <iostream>
#include <string>
using namespace std;

int m, n, s;
string op;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    s = 0;
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> op;

        if (op == "add") {
            cin >> n;
            s |= (1 << n);
        }
        else if (op == "remove") {
            cin >> n;
            s &= ~(1 << n);
        }
        else if (op == "check") {
            cin >> n;
            if (s & (1 << n)) {
                cout << "1\n";
            }
            else {
                cout << "0\n";
            }
        }
        else if (op == "toggle") {
            cin >> n;
            s ^= (1 << n);
        }
        else if (op == "all") {
            s = (1 << 21) - 1;
        }
        else {
            s = 0;
        }   
    }
    return 0;
}