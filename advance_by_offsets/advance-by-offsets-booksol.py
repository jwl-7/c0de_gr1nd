"""Furthest Reach Algorithm

Time Complexity: O(n)
"""

class Solution:
    def can_reach_end(self, A):
        furthest_reach_so_far, last_index = 0, len(A) - 1
        i = 0
        while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
            furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
            i += 1
        return furthest_reach_so_far >= last_index
    
def main():
    s = Solution()
    test_cases = [
        [3, 3, 1, 0, 2, 0, 1],
        [3, 2, 0, 0, 2, 0, 1],
        [0, 0, 1, 10, 6, 0, 1, 6, 0, 10, 1, 0, 4, 3],
        [8, 7, 9, 2, 3, 6, 8, 8, 7, 7, 1, 3, 6, 7, 4, 4, 5, 0, 8, 7],
        [8, 8, 4, 5, 4, 2, 4, 0, 4, 1, 3, 7, 3, 8, 10, 8, 1, 1, 8, 2, 2, 3, 9, 0, 4, 9, 10, 5, 4],
        [0, 2, 6, 10, 9, 10, 3, 3, 10, 0, 7, 6, 4, 3, 3, 10, 10, 4, 0, 7, 3, 0, 5, 4, 5, 7, 9, 0, 10, 1, 4]
        ]
    for num in test_cases:
        can_reach = s.can_reach_end(num)
        print(num)
        print(f'Can advance to end? {can_reach}\n')

if __name__ == '__main__':
    main()