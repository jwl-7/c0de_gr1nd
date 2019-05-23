"""[FILL IN] Algorithm

Time Complexity: [FILL IN]
"""

class Solution:
    def multiply(self, num1, num2):
        # TODO - you fill in here.
        return []
    
def main():
    s = Solution()
    test_cases = [
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 9], [1, 3, 0]),
        ([7, 0, 4, 9], [1, 9, 8, 4]),
        ([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]),
        ([3, 3, 2, 8, 3, 9, 1, 1, 6], [3, 3, 2, 4, 8, 9, 1, 1, 7])
        ]
    for num in test_cases:
        product = s.multiply(num[0], num[1])
        print(f'{num[0]} * {num[1]} = {product}')

if __name__ == '__main__':
    main()