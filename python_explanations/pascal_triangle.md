# Compute Rows in Pascal's Triangle
Write a program which takes as input a nonnegative integer _n_ and returns the first _n_ rows of Pascal's triangle.

## Example
Here is a figure depicting the first five rows of a graphic that is known as Pascal's triangle:
```
        -----
        | 1 |
      ---------
      | 1 | 1 |
    -------------
    | 1 | 2 | 1 |
  -----------------
  | 1 | 3 | 3 | 1 |
---------------------
| 1 | 4 | 6 | 4 | 1 |
---------------------
```
Each row contains one more entry than the previous one. Except for entries in the last row, each entry is adjacent to one or two numbers in the row below it. The first row holds 1. Each entry holds the sum of the numbers in the adjacent entries above it.

## Solution
```python
def generate_pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
```

## Explanation
* Since every entry is the sum of the two values above it, we can use a 2D array and nested loops to calculate those sums.

## Code Dissection
1. Create a 2D array filled with 1's that represents the triangle
    ```python
    triangle = [[1] * (i + 1) for i in range(n)]
    ```
2. Loop over each entry in the triangle that has two values above it
    ```python
    for i in range(n):
        for j in range(1, i):
    ```
3. Set the entry to the sum of the numbers in the adjacent entries above it
    ```python
    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    ```
4. Return the generated Pascal's triangle
    ```python
    return triangle
    ```