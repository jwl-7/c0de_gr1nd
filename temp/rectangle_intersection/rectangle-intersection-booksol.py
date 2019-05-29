"""Rectangle Intersect Check

Time Complexity: O(1)
"""

import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

class Solution:
    def intersect_rectangle(self, R1, R2):
        def is_intersect(R1, R2):
            return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                    and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)

        if not is_intersect(R1, R2):
            return Rectangle(0, 0, -1, -1)  # No intersection.
        return Rectangle(
            max(R1.x, R2.x), max(R1.y, R2.y),
            min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
            min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))
    
def main():
    s = Solution()
    test_cases = [
        ([36, 65, 69, 5], [99, 83, 99, 61]),
        ([26, 12, 76, 62], [68, 59, 77, 28]),
        ([91, 39, 98, 41], [17, 41, 15, 7]),
        ([17, 77, 58, 67], [5, 19, 32, 60]),
        ([82, 44, 65, 47], [83, 91, 61, 40])
        ]
    for num in test_cases:
        intersect = s.intersect_rectangle(Rectangle(num[0][0], num[0][1], num[0][2], num[0][3]), 
                                          Rectangle(num[1][0], num[1][1], num[1][2], num[1][3]))
        print(f'R1 = [{num[0][0]}, {num[0][1]}, {num[0][2]}, {num[0][3]}]')
        print(f'R2 = [{num[1][0]}, {num[1][1]}, {num[1][2]}, {num[1][3]}]')
        print(f'{intersect}\n')

if __name__ == '__main__':
    main()