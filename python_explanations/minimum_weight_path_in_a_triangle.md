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
* Traverse the triangle bottom-up, using the triangle itself as the DP table to keep track of the minimum weight path

## Code Dissection
1. Check if the triangle is empty
    ```python
    if not triangle:
        return 0
    ```
2. Traverse the triangle bottom-up, modifying it in place to keep track of the minimum sum path
    ```python
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    ```
3. Return the top of the triangle (minimum weight path)
    ```python
    return triangle[0][0]
    ```