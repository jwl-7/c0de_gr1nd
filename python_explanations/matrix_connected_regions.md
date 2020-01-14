# Paint a Boolean Matrix
Given an image represented by a binary matrix and a starting position (_x_, _y_), flip the colors of any adjacent cells opposite to the starting color (1 or 0) in the same region. The region is defined by the path that can be navigated from the starting point via the same color.

## Examples
```
 Input: x = 0, y = 0
        [[0, 1, 0],
         [1, 0, 1],
         [0, 1, 1]]
Output: [[1, 1, 0],
         [1, 0, 1],
         [0, 1, 1]]

 Input: x = 1, y = 0
        [[1, 0, 0],
         [1, 1, 0],
         [1, 0, 0]]
Output: [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
```

## Solution
```python
def flip_color(x, y, image):
    color = image[x][y]
    image[x][y] ^= 1
    moves = (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)
    for nxt_x, nxt_y in moves:
        if (
            0 <= nxt_x < len(image) and
            0 <= nxt_y < len(image[nxt_x]) and
            image[nxt_x][nxt_y] == color
        ):
            flip_color(nxt_x, nxt_y, image)
```

## Explanation
* Flip the color at the start position, then try moving left, right, up, and down
* Using a DFS style algorithm, we can travel along a path flipping adjacent entries using the recursive call stack

## Code Dissection
1. Store the color of the starting position, then flip its color
    ```python
    color = image[x][y]
    image[x][y] ^= 1
    ```
2. Define a set of coordinates for moving left, right, up, and down
    ```python
    moves = (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)
    ```
3. Loop through the possible moves, checking if they are the same color as the starting point (_color_), and flip adjacent entries
    ```python
    for nxt_x, nxt_y in moves:
        if (
            0 <= nxt_x < len(image) and
            0 <= nxt_y < len(image[nxt_x]) and
            image[nxt_x][nxt_y] == color
        ):
            flip_color(nxt_x, nxt_y, image)
    ```