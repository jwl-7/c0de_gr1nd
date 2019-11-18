# The Towers of Hanoi Problem
Given a set of 3 pegs with rings on one peg in sorted order (largest on bottom), transfer all the rings to the second peg. You can't put a larger ring on top of a smaller ring.

## Example
```
 Input:                                 Output:

      -|-       |        |                     |       -|-       |
     --|--      |        |                     |      --|--      |
    ---|---     |        |                     |     ---|---     |
----------------------------------      ----------------------------------
       A        B        C                     A        B        C
```

## Solution
```python
def compute_tower_hanoi(num_rings):
    def hanoi(height, source, target, aux):
        if height > 0:
            hanoi(height - 1, source, aux, target)
            result.append([source, target])
            hanoi(height - 1, aux, target, source)

    result = []
    hanoi(num_rings, 0, 1, 2)
    return result
```

## Explanation
1. Move a tower of (height - 1) to the auxiliary pole, using the target pole
2. Move the remaining ring to the target pole
3. Move the tower of (height - 1) from the auxiliary pole to the target pole, using the source pole

## Code Dissection - hanoi
1. Base case: stop recursing when the height of the tower is zero, which is when the tower has been moved to the specified target pole
    ```python
    if height > 0:
    ```
2. Move a tower of (height - 1) to the auxiliary pole, using the target pole
    ```python
    hanoi(height - 1, source, aux, target)
    ```
3. Move the remaining ring to the target pole
    ```python
    result.append([source, target])
    ```
    * This will add to the result list 2 numbers specifying to move a ring from some pole to another
4. Move the tower of (height - 1) from the auxiliary pole to the target pole, using the source pole
    ```python
    hanoi(height - 1, aux, target, source)
    ```

## Code Dissection - compute_tower_hanoi
1. Create a list to store the result
    ```python
    result = []
    ```
    * The elements in _result_ will be in the format [_source_, _target_], which specifies to move a ring on the _source_ pole to the _target_ pole
2. Call the recursive `hanoi()` function
    ```python
    hanoi(num_rings, 0, 1, 2)
    ```
    * This specific statement states that we want to move a tower of rings at pole 0 -> pole 1, and the auxiliary pole is pole 2
3. Return the result list
    ```python
    return result
    ```