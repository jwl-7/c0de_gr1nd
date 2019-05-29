"""Schoolbook Division Algorithm

Time Complexity: O(n)
"""

class Solution:
    def divide(self, x, y):
        quotient = 0
        while x >= y:
            y2 = y
            multiple = 1
            while x >= y2 << 1:
                multiple <<= 1
                y2 <<= 1
            quotient += multiple
            x -= y2
        return quotient
    
def main():
    s = Solution()
    test_cases = [
        (12, 4),
        (7, 7),
        (10, 5),
        (42, 7)
        ]
    for num in test_cases:
        quotient = s.divide(num[0], num[1])
        print(f'{num[0]} / {num[1]} = {quotient}')

if __name__ == '__main__':
    main()