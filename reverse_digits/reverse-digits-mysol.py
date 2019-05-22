"""[FILL IN] Algorithm

Time Complexity: [FILL IN]
"""

class Solution:
    def reverse(self, x):
        return x
    
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