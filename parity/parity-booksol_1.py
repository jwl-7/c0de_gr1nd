"""Brute-Force Algorithm

Time Complexity = O(n), where n is the word size
"""

class Solution:
    def parity(self, x):
        result = 0
        while x:
            result ^= x & 1
            x >>= 1
        return result
    
def main():
    s = Solution()
    test_cases = [
        0b1011,
        0b1001,
        0b100100,
        0b1110000
        ]
    for num in test_cases:
        result = s.parity(num)
        print(f'{bin(num)[2:]} -> {result}')

if __name__ == '__main__':
    main()