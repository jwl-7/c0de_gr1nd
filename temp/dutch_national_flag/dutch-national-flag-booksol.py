"""Quicksort Algorithm

 Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def dutch_flag_partition(self, pivot_index, A):
        pivot = A[pivot_index]
        # Keep the following invariants during partitioning:
        # bottom group: A[:smaller].
        # middle group: A[smaller:equal].
        # unclassified group: A[equal:larger].
        # top group: A[larger:].
        smaller, equal, larger = 0, 0, len(A)
        # Keep iterating as long as there is an unclassified element.
        while equal < larger:
            # A[equal] is the incoming unclassified element.
            if A[equal] < pivot:
                A[smaller], A[equal] = A[equal], A[smaller]
                smaller, equal = smaller + 1, equal + 1
            elif A[equal] == pivot:
                equal += 1
            else:  # A[equal] > pivot.
                larger -= 1
                A[equal], A[larger] = A[larger], A[equal]
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