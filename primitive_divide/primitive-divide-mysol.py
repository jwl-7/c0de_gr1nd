"""Brute-Force Algorithm

Time Complexity: [FILL IN]
"""

class Solution:
    def divide(self, x, y):
        quotient = 0
        while x >= y:
            x -= y
            quotient += 1
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