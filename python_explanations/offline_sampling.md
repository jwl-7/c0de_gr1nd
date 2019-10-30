# Sample Offline Data
This problem is motivated by the need for a company to select a random subset of its customers to roll out a new feature to.

Implement an algorithm that takes as input an array of distinct elements and a size, and returns a subset of the given size of the array of elements. All subsets should be equally likely. Return the result in input array itself.

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