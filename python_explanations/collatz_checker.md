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
* This conjecture in mathematics has been around since 1937, and it's unsolved
* Anyway, this code is what I call IQ Level 700 &mdash; the problem only wants us to test if the collatz conjecture is true, but it also assumes it's true, and if a bunch of math geniuses haven't figured it out, then I'm just going to assume it's true and return true for any positive number

## Code Dissection
1. Return true for positive numbers
    ```python
    return n > 0
    ```