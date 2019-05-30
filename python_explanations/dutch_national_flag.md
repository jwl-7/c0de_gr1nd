# Dutch National Flag Problem
Write a program that takes an array _A_ and an index _i_ into _A_, and rearranges the elements such that all elements less than _A_[_i_] (the "pivot") appear first, followed by the elements equal to the pivot, followed by elements greater than the pivot.  
  
## Examples
```
Before partitioning                 After partitioning
+--------------------------+        +--------------------------+
|           Blue           |        |           Red            |
+--------------------------+        +--------------------------+
|           Red            |        |           White          |
+--------------------------+        +--------------------------+
|           White          |        |           Blue           |
+--------------------------+        +--------------------------+
```
```
Pivot Index: 1
Before: [1, 1, 0, 2]
 After: [0, 1, 1, 2]

Pivot Index: 3
Before: [0, 1, 2, 0, 0, 1, 2]
 After: [0, 0, 0, 2, 1, 2, 1]

Pivot Index: 6
Before: [2, 0, 1, 2, 2, 1, 1, 2, 1]
 After: [0, 1, 1, 1, 1, 2, 2, 2, 2]
```
  
## Solution
```python
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    low = 0
    mid = 0
    high = len(A) - 1
    while mid <= high:
        if A[mid] < pivot:
            A[mid], A[low] = A[low], A[mid]
            low += 1
            mid += 1
        elif A[mid] == pivot:
            mid += 1
        elif A[mid] > pivot:
            A[mid], A[high] = A[high], A[mid]
            high -= 1
```
  
## Explanation
* The solution uses an efficient [quicksort](https://opendatastructures.org/ods-python/11_1_Comparison_Based_Sorti.html#49745) algorithm  
  
## Code Dissection
1. Define variables for the pivot point and 3 pointers used to iterate through the array and swap elements  
    ```python
    pivot = A[pivot_index]
    low = 0
    mid = 0
    high = len(A) - 1
    ```
2. Create a loop that runs until the mid pointer passes the high pointer  
    ```python
    while mid <= high:
    ```
3. If the mid pointer is less than the pivot, swap _A_[mid] and _A_[low], and decrement the low and mid pointers  
    ```python
    if A[mid] < pivot:
        A[mid], A[low] = A[low], A[mid]
        low += 1
        mid += 1
    ```
4. If the mid pointer is equal to the pivot, do not swap anything, and increment the mid pointer  
    ```python
    elif A[mid] == pivot:
        mid += 1
    ```
5. If the mid pointer is greater than the pivot, swap _A_[mid] and _A_[high], and decrement the high pointer  
    ```python
    elif A[mid] > pivot:
        A[mid], A[high] = A[high], A[mid]
        high -= 1
    ```
  
## Step-by-Step Example
* Let _A_ = [1, 1, 0, 2] and pivot_index = 1  

|low, mid|   |   |high|
|-------:|---|---|----|
|      1 | 1 | 0 | 2  |

| low| mid |   |high|
|---:|:---:|---|----|
|  1 |  1  | 0 | 2  |

| low|   | mid |high|
|---:|---|:---:|----|
|  1 | 1 |  0  | 2  |

|   | low |   |mid, high|
|---|:---:|---|---------|
| 0 |  1  | 1 | 2       |

|   | low | high |   |mid|
|---|:---:|:----:|---|---|
| 0 |  1  |  1   | 2 |   |