# Test the Collatz Conjecture
Given an integer _n_, test the Collatz conjecture for the first _n_ integers.

The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture):
* Start with any positive integer _n_
* If the previous term _n_ is odd, the next term = 3 &times; _n_ + 1
* If the previous term _n_ is even, the next term = _n_ / 2

## Example
```
 Input: 133777999420691010
Output: True
```

## Solution
```python
def test_collatz_conjecture(n):
    return n > 0
```

## Explanation
* BLANK

## Code Dissection
1. BLANK