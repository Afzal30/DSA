class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_xor = 2048

        pair_xor = [False] * max_xor
        triplet_xor = [False] * max_xor

        n = len(nums)

        for i in range(n):
            for j in range(i,n):
                pair_xor[nums[i] ^ nums[j]] = True

        for x in range(max_xor):
            if not pair_xor[x]:
                continue

            for v in nums:
                triplet_xor[x^v] = True

        return sum(triplet_xor)

  """
  steps:
brute force is taking every possible triplet (i,j,k) such that i<=j<=k
then compute the triplet xor and store in a set. then the size of the set will be the number of unique xor values.
but total possible triplet = O(n^3) and for n<=1500, it is not possible to generate all triplets.
can we do it in O(n^2) ??
yes
a^b^c = (a^b)^c => associative property
take every possible pair (a,b) and take xor a^b and store
but possible values of a<=1500 and b<=1500.
so total pairs = 1500 * 1500
since nums[i]<=1500 < 2^11 (= 2048). So total possible Xor values are [0..2047] i.e. 2048 total.
though we have 1500*1500 pairs but unique xor values are only 2048.
treat every pair XOR as the first two elements of the triplet.
For every stored XOR value x, XOR it with every element in the array.
Triplet XOR = x ^ nums[k]
time complexity:
total pairs = O(n^2)
unique pair xor values = 2048, we xor with every array element
so it takes 2048*n

so overall = O(n^2 + 2048*n) which equals O(n^2)
"""
