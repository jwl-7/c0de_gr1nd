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
* BLANK

## Code Dissection
1. BLANK