#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int n;
    cin >> n;
    unordered_map<int, string> dict;
    dict[1]="one";dict[2]="two";dict[3]="three";dict[4]="four";dict[5]="five";dict[6]="six";dict[7]="seven";
    dict[8]="eight";dict[9]="nine";
    if (n < 10) {
        cout << dict[n] << endl;
    } else {
        cout << "Greater than 9" << endl;
    }
    return 0;
}
