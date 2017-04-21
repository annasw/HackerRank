#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main() {
    int i;
    long l;
    long long ll;
    char c;
    float f;
    double d;
    cin >> i >> l >> ll >> c >> f >> d;
    cout << i << "\n" << l << "\n" << ll << "\n" << c << "\n";
    cout << fixed << setprecision(3) << f << "\n";
    cout << fixed << setprecision(9) << d << "\n";
    return 0;
}
