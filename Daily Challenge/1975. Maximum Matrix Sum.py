class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totsum = 0
        minabsval = float("inf")
        neg_count = 0

        for row in matrix:
            for ele in row:
                totsum += abs(ele)
                if ele<0:
                    neg_count += 1
                minabsval = min(minabsval,abs(ele))

        if neg_count % 2 !=0 :
            totsum -= 2 * minabsval

        return totsum



# Time Complexity: O(n^2)
# Space Complexity: O(1)

# What this code does?
# Iterates over every element of the matrix.
# Converts each value to its absolute value and adds it to totalSum.
# Counts how many numbers in the matrix are negative.
# Tracks the smallest absolute value in the entire matrix.
# Uses the fact that sign flips affect negatives in pairs.
# If the number of negative values is even, all numbers can be made positive.
# In that case, returns the sum of all absolute values.
# If the number of negative values is odd, one value must stay negative.
# To minimize loss, subtracts 2 × (smallest absolute value) from the total.
# Returns the maximum possible matrix sum after optimal sign flips.
