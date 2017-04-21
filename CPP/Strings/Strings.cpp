#include <iostream>
#include <string>
using namespace std;

int main() {
    string a,b;
    cin >> a >> b;
    
    // Task 1: print the lengths of a and b
    cout << a.size() << " " << b.size() << endl;
    
    // Task 2: print the concatenation of a+b
    cout << a+b << endl;
    
    // Task 3: switch their 0th chars and print a' and b'
    char temp = a[0];
    a[0] = b[0];
    b[0] = temp;
    cout << a << " " << b << endl;
    return 0;
}
