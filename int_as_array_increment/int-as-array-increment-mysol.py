"""Grade School Algorithm

Time Complexity: O(n), where n is the length of A
"""

class Solution:
    def plus_one(self, A):
        # TODO - you fill in here.
        return []
    
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