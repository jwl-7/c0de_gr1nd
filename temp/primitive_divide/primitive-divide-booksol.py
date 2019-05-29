"""Grade-School Division Algorithm

Time Complexity: O(n)
"""

class Solution:
    def divide(self, x, y):
        result, power = 0, 32
        y_power = y << power
        while x >= y:
            while y_power > x:
                y_power >>= 1
                power -= 1

            result += 1 << power
            x -= y_power
        return result
    
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