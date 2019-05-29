"""Reduced Shifts Algorithm

 Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def delete_duplicates(self, A):
        if not A:
            return 0

        write_index = 1
        for i in range(1, len(A)):
            if A[write_index - 1] != A[i]:
                A[write_index] = A[i]
                write_index += 1
        return write_index
    
def main():
    s = Solution()
    test_cases = [
        [-1, -1, 0, 1, 1, 2, 2, 3],
        [-4, -2, -2, 1, 1, 1, 2, 3],
        [2, 3, 5, 5, 7, 11, 11, 11, 13],
        [-4, -3, -3, -2, -1, 0, 1, 2, 2, 3, 3, 4, 5, 5],
        [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4],
        ]
    for num in test_cases:
        print(f'      A = {num}')
        num_valid_elements = s.delete_duplicates(num)
        print(f'Updated = {num}')
        print(f'Valid Elements = {num_valid_elements}\n')

if __name__ == '__main__':
    main()