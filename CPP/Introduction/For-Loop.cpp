#include <iostream>
#include <cstdio>
#include <unordered_map>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    unordered_map<int, string> dict;
    dict[1]="one";dict[2]="two";dict[3]="three";dict[4]="four";dict[5]="five";dict[6]="six";dict[7]="seven";
    dict[8]="eight";dict[9]="nine";
    
    for(int i=a; i<=b; i++) {
        if (i<10) {
            cout << dict[i] << endl;
        }
        else if (i%2==0) {
            cout << "even" << endl;
        }
        else {
            cout << "odd" << endl;
        }
    }
    
    return 0;
}
