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
    def hanoi(ring, source, dest, spare):
        if ring > 0:
            hanoi(ring - 1, source, spare, dest)
            result.append([source, dest])
            hanoi(ring - 1, spare, dest, source)

    result = []
    hanoi(num_rings, 0, 1, 2)
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK