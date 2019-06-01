# Compute the Next Permutation
There exist exactly _n_! permutations of _n_ elements. These can be totally ordered using the _dictionary ordering_ -- define permutation _p_ to appear before permutation _q_ if in the first place where _p_ and _q_ differ in their array representations, starting from index 0, the corresponding entry for _p_ is less than that for _q_.  
  
Write a program that takes as input a permutation, and returns the next permutation under dictionary ordering. If the permutation is the last permutation, return the empty array.  
  
## Examples
```
 Input: [1, 0, 3, 2]
Output: [1, 2, 0, 3]

 Input: [3, 2, 1, 0]
Output: []

 Input: [4, 2, 3, 0, 3, 1, 8, 4]
Output: [4, 2, 3, 0, 3, 4, 1, 8]
```
  
## Solution
```python
def next_permutation(perm):
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    if i == -1:
        return []
    for j in reversed(range(i + 1, len(perm))):
        if perm[j] > perm[i]:
            perm[i], perm[j] = perm[j], perm[i]
            break
    perm[i + 1:len(perm) + 1] = perm[i + 1:len(perm) + 1][::-1]
    return perm
```
  
## Explanation
The general algorithm for computing the next permutation:  
1. Find _i_ such that _p_[_i_] < _p_[_i_ + 1] and entries after index _i_ appear in decreasing order  
2. Find the smallest _p_[_j_] such that _p_[_j_] > _p_[_i_]  (note that _p_[_j_] occurs after _p_[_i_])  
3. Swap _p_[_j_] and _p_[_i_]  
4. Reverse the sequence after position _i_  
  
## Code Dissection
1. Define _i_ to be 2 positions from the last index of perm  
    ```python
    i = len(perm) - 2
    ```
    * _i_ is defined as it is, because perm[_i_] must be less than perm[_i_ + 1], and there must exist a perm[_j_] after perm[_i_ + 1]  
2. Create a loop that finds _i_ such that p[_i_] < p[_i_ + 1] -- iterate from [left <- right]  
    ```python
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    ```
    * ```_i_ >= 0``` ensures that the loop does not run past the beginning of the array  
    * ```perm[_i_] >= perm[_i_ + 1]``` is the case that all entries after index _i_ appear in decreasing order  
3. If _i_ == -1, then perm is the last permutation, and we return an empty array  
    ```python
    if i == -1:
        return []
    ```
4. Iterate over perm [left <- right] from the last index to _i_ + 1 -- this is where we find _j_  
    ```python
    for j in reversed(range(i + 1, len(perm))):
    ```
    * _j_ must exist after _i_, which is why we only iterate to _i_ + 1  
5. If perm[_j_] > perm[_i_], then swap perm[_j_] and perm[_i_]  
    ```python
    if perm[j] > perm[i]:
        perm[i], perm[j] = perm[j], perm[i]
        break
    ```
    * ```break``` is added to stop the loop when _j_ has been found  
6. Reverse the sequence of elements that occur after position _i_  
    ```python
    perm[i + 1:len(perm) + 1] = perm[i + 1:len(perm) + 1][::-1]
    ```
    * ```perm[i + 1:len(perm) + 1]``` defines the range of elements after position _i_  
    * ```[::-1]``` reverses the elements  
7. Return the next permutation  
    ```python
    return perm
    ```
  
## Step-by-Step Example
* Let perm = [4, 2, 3, 0, 3, 1, 8, 4]  
  
1. asdf

|   |   |   |   |   |_i_|   |   |
|---|---|---|---|---|---|---|---|
| 4 | 2 | 3 | 0 | 3 | 1 | 8 | 4 |