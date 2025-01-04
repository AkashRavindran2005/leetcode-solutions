'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30'''

#Solution

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result