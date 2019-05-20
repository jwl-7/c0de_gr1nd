"""Brute-Force Algorithm

Time Complexity: O(n)
"""

class Solution:
    def reverse_bits(self, x):
        return x
    
def main():
    s = Solution()
    test_cases = [
        0b1110000000000001,
        0b1001111000110101,
        0b1001011100111000,
        0b1110011001100000
        ]
    for num in test_cases:
        reversed_num = s.parity(num)
        print(f'{bin(num)[2:]} -> {reversed_num}')

if __name__ == '__main__':
    main()