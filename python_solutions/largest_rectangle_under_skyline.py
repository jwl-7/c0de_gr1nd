from test_framework import generic_test


def calculate_largest_rectangle(heights):
    stack = []
    rectangle = 0
    for i, h in enumerate(heights + [0]):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            rectangle = max(rectangle, width * height)
        stack.append(i)
    return rectangle


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
