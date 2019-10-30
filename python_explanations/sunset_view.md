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
* Since the sun sets in the West, and the buildings are ordered from [East -> West], it is easier to process the input sequence from [right -> left]
* The solution iterates over the sequence in reverse, keeps track of the tallest building so far, and if the current building is taller, the index of the current building is pushed to the sunset list

## Code Dissection
1. Create a list to store the indexes of the buildings that can see the sunset and a variable to store the tallest building so far
    ```python
    sunset = []
    curr_max = 0
    ```
2. Loop over the _sequence_ in reverse
    ```python
    for i in reversed(range(len(sequence))):
    ```
3. If the current building is taller than the tallest building so far, set its height as *curr_max* and push the index of the current building to the _sunset_ list
    ```python
    if sequence[i] > curr_max:
        curr_max = sequence[i]
        sunset.append(i)
    ```
4. Return the list of indexes of buildings that can see the sunset
    ```python
    return sunset
    ```