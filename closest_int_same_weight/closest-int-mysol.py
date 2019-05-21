"""Brute-Force Algorithm

Time Complexity: O(n), where n is the integer width
"""

class Solution:
    def closest_int_same_bit_count(self, x):
        for i in range(63):
            index_i = x >> i & 1
            index_j = x >> i + 1 & 1
            if index_i != index_j:
                x ^= 1 << i
                x ^= 1 << i + 1
                return x
        
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