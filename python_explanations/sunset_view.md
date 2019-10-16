# Compute Buildings with a Sunset View
You are given a series of buildings that have windows facing west. The buildings are in a straight line, and any building which is to the east of a building of equal or greater height cannot view the sunset.

Design an algorithm that processes buildings in east-to-west order and returns the set of buildings which view the sunset. Each building is specified by height.

## Examples
```
 Input: [1, 10, 6, 9, 3]
Output: [4, 3, 1]

 Input: [6, 9, 3, 9, 5, 16, 9, 13]
Output: [7, 5]
```

## Solution
```python
def examine_buildings_with_sunset(sequence):
    sunset = []
    curr_max = 0
    for i in reversed(range(len(sequence))):
        if sequence[i] > curr_max:
            curr_max = sequence[i]
            sunset.append(i)
    return sunset
```

## Explanation
* BLANK

## Code Dissection
1. BLANK