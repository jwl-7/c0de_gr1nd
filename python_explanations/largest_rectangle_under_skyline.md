# Compute the Largest Rectangle Under the Skyline
Given an array of integers that represent the heights of buildings, find the area of the largest rectangle under the skyline. Each building is 1 width.

## Example
<img src='drawio_diagrams/largest_rectangle_under_skyline.svg' width='40%'>

```
 Input: [3, 3, 4, 3, 2]
Output: 12

Size of largest rectangle = 4 * 3 = 12
```

## Solution
```python
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
```

## Explanation
* BLANK

## Code Dissection
1. BLANK