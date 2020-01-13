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
* Use a stack to process the heights of the buildings
* If the stack is empty or the building is taller than the one at the top of the stack, push it to the stack
* If the stack is not empty and the building is shorter than the one at the top of the stack, compute the rectangle and compare it to the max rectangle

## Code Dissection
1. Create an empty stack and initialize the max rectangle area to zero
    ```python
    stack = []
    rectangle = 0
    ```
2. Loop through all the heights of the buildings, but add a sentinel to the end of _heights_ so that all the buildings will be popped from the stack
    ```python
    for i, h in enumerate(heights + [0]):
    ```
3. If the stack is not empty and the building height < top of the stack, calculate the max rectangle that can be made with the current stack
    ```python
    while stack and h < heights[stack[-1]]:
        height = heights[stack.pop()]
        width = i - stack[-1] - 1 if stack else i
        rectangle = max(rectangle, width * height)
    ```
4. If the stack is empty and the building height > top of the stack or we finishing processing a rectangle, append the next building to the top of the stack
    ```python
    stack.append(i)
    ```
5. Return the largest rectangle that can be made under the skyline
    ```python
    return rectangle
    ```