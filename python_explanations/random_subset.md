# Compute a Random Subset
Given a positive integer _n_ and a size-_k_ <= _n_, return a size-_k_ subset of [0, 1, 2, ... , _n_-1].

## Examples
```
n = 10
k = 7
Output1: [2, 9, 1, 4, 6, 8, 7]
Output2: [7, 5, 2, 4, 9, 0, 6]
Output3: [8, 9, 1, 7, 6, 2, 5]

n = 4
k = 4
Output1: [0, 3, 2, 1]
Output2: [3, 2, 1, 0]
Output3: [0, 1, 3, 2]
```

## Solution
```python
def random_subset(n, k):
    subset = random.sample(range(n), k)
    return subset
```

## Explanation
* Create a size-_k_ subset of the sequence [0, ... , _n_-1]

## Code Dissection
1. Use `random.sample(population, k)` to create a size-_k_ subset of the sequence [0, ... , _n_-1]
    ```python
    subset = random.sample(range(n), k)
    ```
    * This would be equivalent to creating a list filled with the numbers [0, ... , _n_-1], then using that list to create the subset
2. Return the random subset
    ```python
    return subset
    ```