"""[FILL IN] Algorithm

Time Complexity: [FILL IN]
"""

class Solution:
    def delete_duplicates(self, A):
        # TODO - you fill in here.
        return 0
    
def main():
    s = Solution()
    test_cases = [
        [-1, -1, 0, 1, 1, 2, 2, 3],
        [-4, -2, -2, 1, 1, 1, 2, 3],
        [-4, -3, -3, -2, -1, 0, 1, 2, 2, 3, 3, 4, 5, 5],
        [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4],
        [-10, -8, -4, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
        ]
    for num in test_cases:
        num_valid_elements = s.delete_duplicates(num)
        print(f'{num}')
        print(f'Valid Elements = {num_valid_elements}\n')

if __name__ == '__main__':
    main()