# Compute the Next Permutation
There exist exactly _n_! permutations of _n_ elements. These can be totally ordered using the _dictionary ordering_ -- define permutation _p_ to appear before permutation _q_ if in the first place where _p_ and _q_ differ in their array representations, starting from index 0, the corresponding entry for _p_ is less than that for _q_.  
  
Write a program that takes as input a permutation, and returns the next permutation under dictionary ordering. If the permutation is the last permutation, return the empty array.  
  
## Examples
```
 Input: [1, 0, 3, 2]
Output: [1, 2, 0, 3]

 Input: [3, 2, 1, 0]
Output: []
```
  
## Solution
```python
def next_permutation(perm):
    # TODO - you fill in here.
    return []
```
  
## Explanation
The general algorithm for computing the next permutation:  
1. Find _i_ such that _p_[_i_] < _p_[_i_ + 1] and entries after index _i_ appear in decreasing order  
2. Find the smallest _p_[_j_] such that _p_[_j_] > _p_[_i_]  (note that _j_ > _i_)  
3. Swap _p_[_j_] and _p_[_i_]  
4. Reverse the sequence after position _i_  
  
## Code Dissection
1. [FILL IN]