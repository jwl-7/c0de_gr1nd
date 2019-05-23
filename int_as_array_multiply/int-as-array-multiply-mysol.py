"""Grade School Algorithm

Time Complexity: O(nm)
"""

class Solution:
    def remove_leading_zeroes(self, num):
        i = 0
        while i < len(num):
            if num[i] > 0:
                break
            num.remove(i)
            i += 1
        return num

    def multiply(self, num1, num2):
        product = [0] * len(num1 + num2)
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                product[i + j + 1] += num1[i] * num2[j]
                product[i + j] += product[i + j + 1] // 10
                product[i + j + 1] %= 10
        product = self.remove_leading_zeroes(product)
        return product
    
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