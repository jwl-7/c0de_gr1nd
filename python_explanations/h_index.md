# Computing the H-Index
Given an array of citations (nonnegative integers), find the [h-index](https://en.wikipedia.org/wiki/H-index). "A scientist has index _h_ if _h_ of his/her _N_ papers have at least _h_ citations each, and the other _N_ − _h_ papers have no more than _h_ citations each."

## Examples
```
 Input: [0, 2, 3, 1, 4]
Output: 2

 Input: [0, 21, 14, 15, 16, 19, 6, 13, 20, 13, 24, 15, 7]
Output: 10
```

## Solution
```python
def h_index(citations):
    n = len(citations)
    citations.sort()
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0
```

## Explanation
* According to the definition, another way to look at this problem is &mdash; find the largest _h_ such that there are _h_ entries in the array >= _h_

## Code Dissection
1. Get the length of the array of citations
    ```python
    n = len(citations)
    ```
2. Sort the array to make finding the _h_-index easier
    ```python
    citations.sort()
    ```
3. Find an element in the array >= _n_ - _i_-th element, and return _n_ - _i_ as the _h_-index
    ```python
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0
    ```