# Find the Length of a Longest Contained Interval
Given an array of integers, find the length of the longest consecutive subsequence.

## Examples
```
   Input: [2, 3, 1, 5]
  Output: 3
Sequence: [2, 3, 1]

   Input: [1, 7, 3, 6, 4, 20, 2]
  Output: 4
Sequence: [1, 3, 4, 2]
```

## Solution
```python
def longest_contained_range(A):
    A = set(A)
    longest = 0
    for x in A:
        if x - 1 not in A:
            y = x + 1
            while y in A:
                y += 1
            longest = max(longest, y - x)
    return longest
```

## Explanation
1. Convert the array into a set of numbers
2. Iterate through the set
3. If the number _x_ is the start of a sequence (_x_ - 1 is not in the set):
    * Test _y_ = _x_ + 1, _x_ + 2, ...
    * Stop at the first _y_ that is not in the set
4. The length of the sequence is _y_ - _x_
5. Compare each length to the longest sequence

## Code Dissection
1. Convert _A_ into a set, and initialize length of the longest sequence
    ```python
    A = set(A)
    longest = 0
    ```
2. Loop over each number in the set
    ```python
    for x in A:
    ```
3. If the number _x_ is the start of a sequence, keep testing for _y_ until _y_ is not in the set
    ```python
    if x - 1 not in A:
        y = x + 1
        while y in A:
            y += 1
    ```
4. Compare the length of the sequence (_y_ - _x_) to the longest length so far
    ```python
    longest = max(longest, y - x)
    ```
5. Return the longest consecutive subsequence
    ```python
    return longest
    ```