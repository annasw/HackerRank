#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

// Did this again for practice with C.

int bubbleSort(int *a, int n);

int bubbleSort(int *a, int n) {
    int totalSwaps = 0;
    int numSwaps;
    do {
        numSwaps = 0;
        for (int i=0; i<n-1; i++) {
            if (a[i]>a[i+1]) {
                int temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
                totalSwaps++;
                numSwaps++;
            }
        }
    } while(numSwaps != 0);
    return totalSwaps;
}

int main(){
    int n; 
    scanf("%d",&n);
    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%d",&a[a_i]);
    }
    int totSwaps = bubbleSort(a, n);
    printf("Array is sorted in %d swaps.\n", totSwaps);
    printf("First Element: %d\n", a[0]);
    printf("Last Element: %d\n",a[n-1]);
    return 0;
}
