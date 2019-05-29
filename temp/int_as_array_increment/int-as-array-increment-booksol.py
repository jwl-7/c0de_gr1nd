"""Grade School Algorithm

Time Complexity: O(n), where n is the length of A
"""

class Solution:
    def plus_one(self, A):
        A[-1] += 1
        for i in reversed(range(1, len(A))):
            if A[i] != 10:
                break
            A[i] = 0
            A[i - 1] += 1
        if A[0] == 10:
            # There is a carry-out, so we need one more digit to store the result.
            # A slick way to do this is to append a 0 at the end of the array,
            # and update the first entry to 1.
            A[0] = 1
            A.append(0)
        return A
    
def main():
    s = Solution()
    test_cases = [
        [1, 2, 9],
        [9, 9, 9, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [3, 4, 5, 7, 4, 2, 9, 0, 9, 6, 6, 1, 1],
        ]
    for num in test_cases:
        print(f'{num} -> {s.plus_one(num)}')

if __name__ == '__main__':
    main()