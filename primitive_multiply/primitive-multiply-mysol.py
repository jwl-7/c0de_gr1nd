"""Shift and Add Algorithm

Time Complexity: O(n^2)
"""

class Solution:
    def add(self, x, y):
        while y != 0:
            carry = x & y
            x ^= y
            y = carry << 1
        return x

    def multiply(self, x, y):
        product = 0
        while y != 0:
            if y & 1:
                product = self.add(product, x)
            x <<= 1
            y >>= 1
        return product
    
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