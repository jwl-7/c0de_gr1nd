"""String Slicing Algorithm

Time Complexity: O(n), where n is the number of digits
"""

class Solution:
    def reverse(self, x):
        if x < 0:
            x = str(abs(x))[::-1]
            x = -int(x)
            return x
        else:
            x = str(x)[::-1]
            return int(x)
    
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