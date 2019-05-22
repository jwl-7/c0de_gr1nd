"""Rectangle Nonempty Intersection Checker

Time Complexity: O(1)
"""

import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

class Solution:
    def intersect_rectangle(self, R1, R2):
        # TODO - you fill in here.
        return Rectangle(0, 0, 0, 0)
    
def main():
    s = Solution()
    test_cases = [
        ([36, 65, 69, 5], [99, 83, 99, 61]),
        ([26, 12, 76, 62], [68, 59, 77, 28]),
        ([91, 39, 98, 41], [17, 41, 15, 7]),
        ([17, 77, 58, 67], [5, 19, 32, 60])
        ]
    for num in test_cases:
        intersect = s.intersect_rectangle(Rectangle(num[0][0],num[0][1],num[0][2],num[0][3]), 
                                          Rectangle(num[1][0],num[1][1],num[1][2],num[1][3]))
        print(intersect)

if __name__ == '__main__':
    main()