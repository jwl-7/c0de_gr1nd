"""Shift and Add Algorithm

Time Complexity: O(n^2)
"""

class Solution:
    def multiply(self, x, y):
        def add(a, b):
            while b:
                carry = a & b
                a, b = a ^ b, carry << 1
            return a

        running_sum = 0
        while x:  # Examines each bit of x.
            if x & 1:
                running_sum = add(running_sum, y)
            x, y = x >> 1, y << 1
        return running_sum
        
def main():
    s = Solution()
    test_cases = [
        (3, 4),
        (7, 7),
        (5, 2),
        (10, 8)
        ]
    for num in test_cases:
        product = s.multiply(num[0], num[1])
        print(f'{num[0]} * {num[1]} = {product}')

if __name__ == '__main__':
    main()