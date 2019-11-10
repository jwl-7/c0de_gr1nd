# Enumerate Numbers of the Form _a_ &plus; _b_ &radic;2
Given an integer _k_, compute the _k_ smallest numbers for _a_ &plus; _b_ &radic;2 where _a_ and _b_ are nonnegative integers.

## Example
```
 Input: k = 4
Output: [0.0, 1.0, 1.4142135623730951, 2.0]
```

## Solution
```python
class Number:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * (2 ** (1 / 2))


def generate_first_k_a_b_sqrt2(k):
    nums = SortedDict()
    nums[0.0] = Number(0, 0)
    result = []
    while len(result) < k:
        nxt = nums.popitem(0)[1]
        result.append(nxt.val)
        a = Number(nxt.a + 1, nxt.b)
        b = Number(nxt.a, nxt.b + 1)
        nums[a.val] = a
        nums[b.val] = b
    return result
```

## Explanation
* The advantage of using a BST for this problem is we need to constantly extract a minimum value from a set of numbers while avoiding duplicates
* The `Number` class is used to not only provide an easy computation for our formula, but it keeps track of the _a_ and _b_ of the number at the time of insertion
* `(2 ** (1 / 2))` = &radic;2

## Code Dissection
1. Initialize a BST to hold the minimum numbers (will also not store duplicates)
    ```python
    nums = SortedDict()
    ```
2. Put the first computed value in the tree&mdash;when _a_ and _b_ are both 0
    ```python
    nums[0.0] = Number(0, 0)
    ```
3. Create an empty list to store the _k_ numbers
    ```python
    result = []
    ```
4. Loop until our result list has _k_ numbers in it
    ```python
    while len(result) < k:
    ```
5. Remove the minimum item from the tree, and put its value in _result_
    ```python
    nxt = nums.popitem(0)[1]
    result.append(nxt.val)
    ```
6. Using the previous minimum item _nxt_, create 2 new numbers in which its _a_ or _b_ are incremented by 1
    ```python
    a = Number(nxt.a + 1, nxt.b)
    b = Number(nxt.a, nxt.b + 1)
    ```
7. Insert both new numbers into the tree
    ```python
    nums[a.val] = a
    nums[b.val] = b
    ```
8. Return the _k_ smallest numbers
    ```python
    return result
    ```