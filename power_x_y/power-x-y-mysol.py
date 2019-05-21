"""Iterative Algorithm

Time Complexity: O(n)
"""

class Solution:
    def power(self, x, y):
        result = 1
        if y < 0:
            y = -y
            x = 1 / x
        while y:
            if y & 1:
                result *= x
            x *= x
            y >>= 1
        return result
    
def main():
    s = Solution()
    test_cases = [
        (9.871778445549765, 3),
        (1.0005205926241314, 2),
        (3.398860582608009, 4),
        (11.274393136707644, 5)
        ]
    for num in test_cases:
        result = s.power(num[0], num[1])
        print(f'{num[0]} ^ {num[1]} = {result}')

if __name__ == '__main__':
    main()