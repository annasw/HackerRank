#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, q; // size of base array and # of queries
    cin >> n >> q;
    // We actually never need vectors; this can be just a 2D array,
    // since we get the dimensions of each array before initialization.
    // But we'll use vectors anyway, for practice.
    vector<int> arr[n];
    // Fill the array of vectors
    for (int i=0; i<n; i++) {
        int k;
        cin >> k;
        // Fill in
        vector<int> v;
        // Fill the vector
        for (int j=0; j<k; j++) {
            int elt;
            cin >> elt;
            v.push_back(elt);
        }
        arr[i] = v;
    }
    // Handle queries
    for (int x=0; x<q; x++) {
        int i, j;
        cin >> i >> j;
        cout << arr[i][j] << endl;
    }
    return 0;
}
