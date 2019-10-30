# Advancing Through an Array
In a particular board game, a player has to try to advance through a sequence of positions. Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move. You begin at the first position, and win by getting to the last position.

Write a program which takes an array of _n_ integers, where _A_[_i_] denotes the maximum you can advance from index _i_, and returns whether it is possible to advance to the last index starting from the beginning of the array.

## Examples
```
[3, 3, 1, 0, 2, 0, 1] = True, a valid advance sequence is: 0 -> 1 -> 4 -> 6 -> 6
[3, 2, 0, 0, 2, 0, 1] = False
```

## Solution
```python
def can_reach_end(A):
    furthest = 0
    end = len(A) - 1
    i = 0
    while i <= furthest and furthest < end:
        furthest = max(furthest, A[i] + i)
        i += 1
    return furthest >= end
```

## Explanation
* The approach is to advance as far as possible in each step, while iterating through all the entries in _A_, so that all possible steps are considered

## Code Dissection
1. Initialize variables to help advance through _A_
    ```python
    furthest = 0
    end = len(A) - 1
    i = 0
    ```
    * `furthest` is used to store the furthest index reached so far
    * `end` represents the last index of _A_
    * `i` is used to iterate through _A_
2. Loop while the current index is before the furthest reached, and the furthest index reached is before the end
    ```python
    while i <= furthest and furthest < end:
    ```
3. Iterate through each entry in _A_, and track the furthest index that can be reached
    ```python
    furthest = max(furthest, A[i] + i)
    i += 1
    ```
    * The furthest index _i_ that can be reached from the current index _i_ = _A_[_i_] + _i_
4. Return whether or not it is possible to advance to the end of the array _A_
    ```python
    return furthest >= end
    ```
    * If the furthest index reached >= the last index, this statement returns True

## Step-by-Step Example
* Let _A_ = [3, 3, 1, 0, 2, 0, 1]
* For the tables below, let _i_ = current index and f = furthest index reached so far

|f, i|   |   |   |   |   |   |
|---:|---|---|---|---|---|---|
|  3 | 3 | 1 | 0 | 2 | 0 | 1 |

|   | i |   | f |   |   |   |
|---|---|---|---|---|---|---|
| 3 | 3 | 1 | 0 | 2 | 0 | 1 |

|   |   | i |   | f |   |   |
|---|---|---|---|---|---|---|
| 3 | 3 | 1 | 0 | 2 | 0 | 1 |

|   |   |   | i | f |   |   |
|---|---|---|---|---|---|---|
| 3 | 3 | 1 | 0 | 2 | 0 | 1 |

|   |   |   |   |f, i |   |   |
|---|---|---|---|:---:|---|---|
| 3 | 3 | 1 | 0 |  2  | 0 | 1 |

|   |   |   |   |   | i | f |
|---|---|---|---|---|---|---|
| 3 | 3 | 1 | 0 | 2 | 0 | 1 |