# Find the Minimum Weight Path in a Triangle
Given a triangle of numbers, find the minimum path from top to bottom. You can only move to adjacent numbers in the triangle.

## Example
```
Input:
            -----
            | 2 |
          ---------
          | 3 | 4 |
        -------------
        | 5 | 7 | 6 |
      -----------------
      | 2 | 1 | 4 | 3 |
    ---------------------

Output: 11

2 + 3 + 5 + 1 = 11
```

## Solution
```python
def minimum_path_weight(triangle):
    if not triangle:
        return 0
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]
```

## Explanation
* BLANK

## Code Dissection
1. BLANK