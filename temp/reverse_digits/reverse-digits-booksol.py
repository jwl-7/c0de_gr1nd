"""No String Algorithm

Time Complexity: O(n), where n is the number of digits
"""

class Solution:
    def reverse(self, x):
        result, x_remaining = 0, abs(x)
        while x_remaining:
            result = result * 10 + x_remaining % 10
            x_remaining //= 10
        return -result if x < 0 else result
    
def main():
    s = Solution()
    test_cases = [
        42,
        -314,
        2117,
        -94,
        77,
        52392,
        12345789
        ]
    for num in test_cases:
        reversed_num = s.reverse(num)
        print(f'{num} -> {reversed_num}')

if __name__ == '__main__':
    main()