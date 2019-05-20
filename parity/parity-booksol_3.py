"""Lookup Table Algorithm

Time Complexity = O(log n), where n is the word size
"""

class Solution:
    def parity(self, x):
        x ^= x >> 32
        x ^= x >> 16
        x ^= x >> 8
        x ^= x >> 4
        x ^= x >> 2
        x ^= x >> 1
        return x & 0x1
    
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