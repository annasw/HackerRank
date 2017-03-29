import java.util.*;

/**
 * DOES NOT WORK
 * (Not-so-)Temporary placeholder until I can upload a solution that does.
 * The logic is solid, my understanding of the data structures involved is fine,
 * I just am out of practice implementing this stuff in Java.
 */

public class Solution {
    Map<String, Integer> magazineMap;
    Map<String, Integer> noteMap;
    
    public Solution(String magazine, String note, int m, int n) {
        String[] magWords = new String[m];
        magWords = magazine.split(" ");
        String[] noteWords = new String[n];
        noteWords = note.split(" ");
        
        for (int i=0; i<m; i++) {
            if (!magazineMap.containsKey(magWords[i])) {
                magazineMap.put(magWords[i], 1);
            }
            else {
                magazineMap.put(magWords[i], magazineMap.get(magWords[i])+1);
            }
        }
        for (int i=0; i<n; i++) {
            if (!noteMap.containsKey(noteWords[i])) {
                noteMap.put(noteWords[i], 1);
            }
            else {
                noteMap.put(noteWords[i], noteMap.get(noteWords[i])+1);
            }
        }
    }
    
    public boolean solve() {
        boolean works = true;
        
        Set<Map.Entry<String, Integer>> noteSet = noteMap.entrySet();
        Iterator it = noteSet.iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry) it.next();
            String k = (String) pair.getKey();
            int v = (int) pair.getValue();
            if (magazineMap.containsKey(k)) {
                int magValue = magazineMap.get(k);
                if (v>magValue) {
                    works = false;
                    break;
                }
            } else {
                works = false;
                break;
            }
        }
        
        return works;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        
        // Eat whitespace to beginning of next line
        scanner.nextLine();
        
        Solution s = new Solution(scanner.nextLine(), scanner.nextLine(), m, n);
        scanner.close();
        
        boolean answer = s.solve();
        if(answer)
            System.out.println("Yes");
        else System.out.println("No");
      
    }
}
