# Implement a Sudoku Solver
Given a sudoku board represented by a 9 &times; 9 2D array, solve the board. 0's in the array represent blank spots.

## Example
```
 Input: [[0, 7, 0, 0, 0, 0, 1, 3, 0],
         [0, 0, 0, 9, 2, 7, 0, 6, 0],
         [4, 0, 0, 0, 0, 0, 0, 8, 9],
         [3, 0, 1, 0, 5, 0, 6, 4, 0],
         [0, 0, 8, 4, 0, 9, 2, 0, 0],
         [0, 0, 7, 1, 6, 0, 5, 0, 0],
         [0, 2, 0, 0, 9, 1, 0, 0, 7],
         [0, 0, 5, 8, 0, 0, 0, 0, 0],
         [6, 3, 0, 2, 0, 0, 0, 0, 4]]

Output: [[9, 7, 6, 5, 8, 4, 1, 3, 2],
         [1, 8, 3, 9, 2, 7, 4, 6, 5],
         [4, 5, 2, 3, 1, 6, 7, 8, 9],
         [3, 9, 1, 7, 5, 2, 6, 4, 8],
         [5, 6, 8, 4, 3, 9, 2, 7, 1],
         [2, 4, 7, 1, 6, 8, 5, 9, 3],
         [8, 2, 4, 6, 9, 1, 3, 5, 7],
         [7, 1, 5, 8, 4, 3, 9, 2, 6],
         [6, 3, 9, 2, 7, 5, 8, 1, 4]]
```

## Solution
```python
def solve_sudoku(board):
    def is_valid_move(board, row, col, move):
        if any(board[row][i] == move for i in range(9)):
            return False
        if any(board[j][col] == move for j in range(9)):
            return False

        block_row = 3 * (row // 3)
        block_col = 3 * (col // 3)

        if any(
            board[i][j] == move
            for i in range(block_row, block_row + 3)
            for j in range(block_col, block_col + 3)
        ):
            return False
        return True

    def backtrack(board, row, col):
        while board[row][col]:
            col += 1
            if col == 9:
                col = 0
                row += 1
            if row == 9:
                return True

        for x in range(1, 10):
            if is_valid_move(board, row, col, x):
                board[row][col] = x
                if backtrack(board, row, col):
                    return True

        board[row][col] = 0
        return False

    backtrack(board, 0, 0)
```

## Explanation
* The logic of the solution is simple: go to the next empty space, try all possible moves, and backtrack if it doesn't work
* To validate a move:
    1. Check the row
    2. Check the column
    3. Check the block

## Code Dissection - is_valid_move
1. Check the row to make sure that the number (move) does not already exist
    ```python
    if any(board[row][i] == move for i in range(9)):
        return False
    ```
2. Check the column to make sure that the number (move) does not already exist
    ```python
    if any(board[j][col] == move for j in range(9)):
        return False
    ```
3. Compute the first row and first column of the block
    ```python
    block_row = 3 * (row // 3)
    block_col = 3 * (col // 3)
    ```
4. Check the block to make sure that the number (move) does not already exist
    ```python
    if any(
            board[i][j] == move
            for i in range(block_row, block_row + 3)
            for j in range(block_col, block_col + 3)
        ):
        return False
    ```
5. If the move gets past all 3 checks, then the move is valid
    ```python
    return True
    ```

## Code Dissection - backtrack
1. Search for the next empty space
    ```python
    while board[row][col]:
        col += 1
        if col == 9:
            col = 0
            row += 1
        if row == 9:
            return True
    ```
2. Try all possible moves, and backtrack if it doesn't work
    ```python
    for x in range(1, 10):
        if is_valid_move(board, row, col, x):
            board[row][col] = x
            if backtrack(board, row, col):
                return True
    ```
3. If there is no valid number for the current space, then reset its entry and backtrack
    ```python
    board[row][col] = 0
    return False
    ```

## Code Dissection - solve_sudoku
1. Run `backtrack()` starting at the first space on the board (0, 0)
    ```python
    backtrack(board, 0, 0)
    ```