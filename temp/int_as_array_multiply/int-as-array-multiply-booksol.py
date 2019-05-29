"""Grade School Algorithm

Time Complexity: O(nm)
"""

class Solution:
    def multiply(self, num1, num2):
        sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
        num1[0], num2[0] = abs(num1[0]), abs(num2[0])

        result = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                result[i + j + 1] += num1[i] * num2[j]
                result[i + j] += result[i + j + 1] // 10
                result[i + j + 1] %= 10

        # Remove the leading zeroes.
        result = result[next((
            i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
        return [sign * result[0]] + result[1:]
    
def main():
    s = Solution()
    test_cases = [
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 9], [1, 3, 0]),
        ([-7, 0, 4, 9], [-1, 9, 8, 4]),
        ([-6, 1, 3, 7, 8], [4, 5, 2, 4, 9]),
        ([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]),
        ([3, 3, 2, 8, 3, 9, 1, 1, 6], [3, 3, 2, 4, 8, 9, 1, 1, 7])
        ]
    for num in test_cases:
        product = s.multiply(num[0], num[1])
        print(f'{num[0]} * {num[1]} = {product}')

if __name__ == '__main__':
    main()