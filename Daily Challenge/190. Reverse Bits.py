class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0xffffffff
        n_bits = n & mask
        binary_str = format(n_bits, '032b')
        return int(binary_str[::-1], 2)
