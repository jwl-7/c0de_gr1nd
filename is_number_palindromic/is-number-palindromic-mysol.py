"""[FILL IN] Algorithm

Time Complexity: [FILL IN]
"""

class Solution:
    def is_palindrome_number(self, x):
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