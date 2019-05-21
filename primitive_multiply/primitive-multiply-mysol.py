"""Shift and Add Algorithm

Time Complexity: O(n^2)
"""

class Solution:
    def add(self, x, y):
        while y != 0:
            carry = x & y
            x ^= y
            y = carry << 1
        return x

    def multiply(self, x, y):
        result_sum = 0
        while y != 0:
            if y & 1:
                result_sum = self.add(result_sum, x)
            x <<= 1
            y >>= 1
        return result_sum
    
def main():
    s = Solution()
    test_cases = [
        (3, 4),
        (7, 7),
        (5, 2),
        (10, 8)
        ]
    for num in test_cases:
        result_sum = s.multiply(num[0], num[1])
        print(f'{num[0]} * {num[1]} = {result_sum}')

if __name__ == '__main__':
    main()