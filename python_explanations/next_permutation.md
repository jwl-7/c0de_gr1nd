# Compute the Next Permutation
Given a permutation, return the next permutation under dictionary ordering. If the permutation is the last, then return an empty array.

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
    while i >= 0 and perm[i] >= perm[i+1]:
        i -= 1

    if i == -1:
        return []

    for j in reversed(range(i+1, len(perm))):
        if perm[j] > perm[i]:
            perm[i], perm[j] = perm[j], perm[i]
            break

    perm[i+1 : len(perm)+1] = perm[i+1 : len(perm)+1][::-1]
    return perm
```

## Explanation
The algorithm for computing the next permutation:
1. Find _i_ such that _p_[_i_] < _p_[_i_+1] and entries after index _i_ appear in decreasing order
2. Find the smallest _p_[_j_] such that _p_[_j_] > _p_[_i_]  (note that _p_[_j_] occurs after _p_[_i_])
3. Swap _p_[_j_] and _p_[_i_]
4. Reverse the sequence after position _i_

## Code Dissection
1. Define _i_ to be 2 positions before last index of _perm_
    ```python
    i = len(perm) - 2
    ```
    * _i_ is defined as it is, because _perm_[_i_] must be less than _perm_[_i_+1], and there must exist a _perm_[_j_] after _perm_[_i_+1]
2. Create a loop that finds _i_ such that _p_[_i_] < _p_[_i_+1] &mdash; iterate from [right -> left]
    ```python
    while i >= 0 and _perm_[i] >= _perm_[i+1]:
        i -= 1
    ```
    * `i >= 0` ensures that the loop does not run past the beginning of the array
    * `perm[i] >= perm[i+1]` is the case that all entries after index _i_ appear in decreasing order
3. If _i_ == -1, then perm is the last permutation, so return an empty array
    ```python
    if i == -1:
        return []
    ```
4. Iterate over _perm_ [right -> left] from the last index to _i_ + 1 &mdash; this is where we find _j_
    ```python
    for j in reversed(range(i + 1, len(perm))):
    ```
    * _j_ must exist after _i_, which is why we only iterate to _i_ + 1
5. If _perm_[_j_] > _perm_[_i_], then swap _perm_[_j_] and _perm_[_i_]
    ```python
    if perm[j] > perm[i]:
        perm[i], perm[j] = perm[j], perm[i]
        break
    ```
    * `break` is added to stop the loop when _j_ has been found
6. Reverse the sequence of elements that occur after position _i_
    ```python
    perm[i+1 : len(perm)+1] = perm[i+1 : len(perm)+1][::-1]
    ```
    * `perm[i+1 : len(perm)+1]` defines the range of elements after position _i_
    * `[::-1]` reverses the elements
7. Return the next permutation
    ```python
    return perm
    ```

## Step-by-Step Example
* Let perm = [7, 5, 6, 8, 8, 3, 2, 1]

##### _i_ starts 2 positions before last index
|   |   |   |   |   |_i_|   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### 8 > 3, continue
|   |   |   |   |_i_|   |   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### 8 >= 8, continue
|   |   |   |_i_|   |   |   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### 6 < 8, _i_ has been found
|   |   |_i_|   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### _j_ starts at last index
|   |   |_i_|   |   |   |   |_j_|
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### 2 < 6, continue
|   |   |_i_|   |   |   |_j_|   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### 3 < 6, continue
|   |   |_i_|   |   |_j_|   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### 8 > 6, _j_ has been found
|   |   |_i_|   |_j_|   |   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 6 | 8 | 8 | 3 | 2 | 1 |

##### swap _i_ and _j_
|   |   |_i_|   |_j_|   |   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 8 | 8 | 6 | 3 | 2 | 1 |

##### reverse sequence after _i_
|   |   |_i_|   |_j_|   |   |   |
|---|---|---|---|---|---|---|---|
| 7 | 5 | 8 | 1 | 2 | 3 | 6 | 8 |

Output: [7, 5, 8, 1, 2, 3, 6, 8]