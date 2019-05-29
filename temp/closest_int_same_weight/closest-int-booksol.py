"""Brute-Force Algorithm

Time Complexity: O(n), where n is the integer width
"""

class Solution:
    def closest_int_same_bit_count(self, x):
        NUM_UNSIGNED_BITS = 64
        for i in range(NUM_UNSIGNED_BITS - 1):
            if (x >> i) & 1 != (x >> (i + 1)) & 1:
                x ^= (1 << i) | (1 << (i + 1))  # Swaps bit-i and bit-(i + 1).
                return x

        # Raise error if all bits of x are 0 or 1.
        raise ValueError('All bits are 0 or 1')
        
def main():
    s = Solution()
    test_cases = [
        92,
        55,
        69,
        74
        ]
    for num in test_cases:
        closest_int = s.closest_int_same_bit_count(num)
        print(f'{num} -> {closest_int}')

if __name__ == '__main__':
    main()