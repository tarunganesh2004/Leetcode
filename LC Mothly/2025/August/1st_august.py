# Pascals Traingle LC 118

numRows=5

def generate(numRows):
    if numRows==0:
        return []
    
    res=[]
    first_row=[1]
    res.append(first_row)

    for i in range(1,numRows):
        prev_row=res[i-1]
        new_row=[1]
        for j in range(1,i):
            new_row.append(prev_row[j-1]+prev_row[j])
        new_row.append(1)
        res.append(new_row)

    return res

print(generate(numRows))

"""
Java Solution
import java.util.*;
public static List<List<Integer>> pascalTriangle(int n) {
        List<List<Integer>> res = new ArrayList<>();
        if (n == 0) {
            return res;
        }
        // first row is [1]
        List<Integer> firstRow = new ArrayList<>();
        firstRow.add(1);
        res.add(firstRow);

        for (int i = 1; i < n; i++) {
            List<Integer> prevRow = res.get(i - 1);
            List<Integer> currentRow = new ArrayList<>();
            // first element of the row is always 1
            currentRow.add(1);
            // calculate the values in between
            for (int j = 1; j < i; j++) {
                int value = prevRow.get(j - 1) + prevRow.get(j);
                currentRow.add(value);
            }
            // last element of the row is always 1
            currentRow.add(1);
            // add the current row to the result
            res.add(currentRow);
        }
        return res;
    }
"""