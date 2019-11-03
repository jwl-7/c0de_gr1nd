# Sample Offline Data
Given an array _A_ of distinct integers, return a subset of _A_ of the given size _k_.

## Examples
```
k = 3
A = [1, 2, 3, 4]
Output1: [3, 2, 1]
Output2: [4, 3, 2]
Output3: [1, 2, 3]

k = 5
A = [1, 2, 3, 4, 5, 6, 7]
Output1: [6, 1, 3, 5, 7]
Output2: [4, 3, 2, 1, 5]
Output3: [1, 6, 7, 2, 4]
```

## Pythonic Solution
```python
def random_sampling(k, A):
    A[:] = random.sample(A, k)
```

## Explanation
* Rather than looping over _A_ and swapping at random indexes, the solution uses a built-in function from the random module that performs exactly what we need

## Pythonic Code Dissection
1. Use `random.sample(population, k)` to change _A_ to a random subset of size _k_
    ```python
    A[:] = random.sample(A, k)
    ```