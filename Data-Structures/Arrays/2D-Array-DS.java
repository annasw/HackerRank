import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int arr_i=0; arr_i < 6; arr_i++){
            for(int arr_j=0; arr_j < 6; arr_j++){
                arr[arr_i][arr_j] = in.nextInt();
            }
        }
        /* To deal with case where maxValue < 0, we need to start with maxValue set to something besides 0 */
        int maxValue = arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2];
        for(int y=0; y<4; y++) {
            for(int x=0; x<4; x++) {
                int tempSum = arr[y][x]+arr[y][x+1]+arr[y][x+2]+arr[y+1][x+1]+arr[y+2][x]+arr[y+2][x+1]+arr[y+2][x+2];
                if (tempSum > maxValue) {maxValue = tempSum;}
            }
        }
        System.out.print(maxValue);
    }
}
