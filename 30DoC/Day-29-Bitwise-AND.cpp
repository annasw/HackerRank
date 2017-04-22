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

int maxAnd(int n, int k) {
    int maxVal = 0;
    for (int a=1; a<n; a++) {
        for (int b=a+1; b<=n; b++) {
            int bitAnd = a&b; // avoids weird behavior with & operator
            if (bitAnd==k-1) {return bitAnd;} // if we find the max theoretical value, we're done
            else {
                if (bitAnd < k) {maxVal = max(maxVal, bitAnd);}
            }
        }
    }
    return maxVal;
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        int k;
        cin >> n >> k;
        
        cout << maxAnd(n,k) << endl;
    }
    return 0;
}
