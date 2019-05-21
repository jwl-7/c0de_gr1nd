"""(FILL IN) Algorithm

Time Complexity: (FILL IN)
"""

class Solution:
    def add(self, x, y):
        while y != 0:
            carry = x & y
            x ^= y
            y = carry << 1
        return x

    def multiply(self, x, y):
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