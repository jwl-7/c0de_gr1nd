"""Quicksort Based Algorithm

Time Complexity: O(n)
"""

class Solution:
    def dutch_flag_partition(self, pivot_index, A):
        pivot = A[pivot_index]
        low = 0
        mid = 0
        high = len(A) - 1
        while mid <= high:
            if A[mid] < pivot:
                A[mid], A[low] = A[low], A[mid]
                low += 1
                mid += 1
            elif A[mid] == pivot:
                mid += 1
            elif A[mid] > pivot:
                A[mid], A[high] = A[high], A[mid]
                high -= 1
        return A

    
def main():
    s = Solution()
    test_cases = [
        (1, [1, 1, 0, 2]),
        (3, [0, 1, 2, 0, 0, 1, 2]),
        (0, [2, 0, 1, 0, 1, 0, 2, 0]),
        (6, [2, 0, 1, 2, 2, 1, 1, 2, 1]),
        (8, [2, 0, 1, 2, 2, 0, 2, 2, 1, 2, 1, 1, 2, 1])
        ]
    for num in test_cases:
        print(f'PIVOT INDEX: {num[0]}')
        print(f'BEFORE: {num[1]}')
        flag = s.dutch_flag_partition(num[0], num[1])
        print(f'AFTER: {flag}\n')

if __name__ == '__main__':
    main()