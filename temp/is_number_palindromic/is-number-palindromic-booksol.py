"""Direct Extract Algorithm

 Time Complexity: O(n)
Space Complexity: O(1)
"""

import math

class Solution:
    def is_palindrome_number(self, x):
        if x <= 0:
            return x == 0

        num_digits = math.floor(math.log10(x)) + 1
        msd_mask = 10**(num_digits - 1)
        for i in range(num_digits // 2):
            if x // msd_mask != x % 10:
                return False
            x %= msd_mask  # Remove the most significant digit of x.
            x //= 10  # Remove the least significant digit of x.
            msd_mask //= 100
        return True
    
def main():
    s = Solution()
    test_cases = [
        0,
        1,
        7,
        11,
        2147412,
        923193,
        -1,
        100,
        2112,
        214745,
        777
        ]
    for num in test_cases:
        is_palindrome = s.is_palindrome_number(num)
        print(f'{num} -> {is_palindrome}')

if __name__ == '__main__':
    main()