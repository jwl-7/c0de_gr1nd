"""Brute-Force Algorithm

Time Complexity: O(n)
"""

class Solution:
    def reverse_bits(self, x):
        return x
    
def main():
    s = Solution()
    test_cases = [
        0b1011,
        0b1001,
        0b100100,
        0b1110000
        ]
    for num in test_cases:
        reversed_num = s.parity(num)
        print(f'{bin(num)[2:]} -> {reversed_num}')

if __name__ == '__main__':
    main()