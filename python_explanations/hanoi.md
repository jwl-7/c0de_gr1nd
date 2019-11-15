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

Output:
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

## Code Dissection
1. BLANK