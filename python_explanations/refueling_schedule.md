# The Gasup Problem
There are _n_ cities on a circular route. Given the amount of gas at each city and the distance to each city, find the city which allows you to travel the entire route after refilling an empty gas tank. The amount of gas is in gallons, the distances are in miles, and the car gets 20 MPG.

## Examples
```
 Input: gallons   = [4, 1, 2, 3]
        distances = [40, 60, 60, 40]
Output: 3

 Input: gallons   = [1, 5, 4, 2, 6, 7, 1]
        distances = [40, 60, 140, 60, 80, 60, 80]
Output: 4
```

## Solution
```python
MPG = 20


def find_ample_city(gallons, distances):
    start = 0
    gas = 0
    for i in range(len(gallons)):
        gas += gallons[i] - distances[i] // MPG
        if gas < 0:
            start = i + 1
            gas = 0
    return start
```

## Explanation
* BLANK

## Code Dissection
1. BLANK