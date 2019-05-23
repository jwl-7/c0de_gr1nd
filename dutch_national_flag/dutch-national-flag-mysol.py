"""[FILL IN] Algorithm

Time Complexity: [FILL IN]
"""

class Solution:
    def dutch_flag_partition(self, pivot_index, A):
        less = []
        equal = []
        greater = []
        pivot = A[pivot_index]
        for i in range(len(A)):
            if A[i] < pivot:
                less.append(A[i])
            elif A[i] == pivot:
                equal.append(A[i])
            elif A[i] > pivot:
                greater.append(A[i])
        A = less + equal + greater
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