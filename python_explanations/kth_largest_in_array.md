# Find the *k*th Largest Element
Design an algorithm for computing the *k*th largest element in an array.

## Examples
```
 Input: k = 2
        [2, -2, 1]
Output: 1

 Input: k = 7
        [3, -5, -3, 3, 3, 2, -8, -3]
Output: -5
```

## Solution
```python
def find_kth_largest(k, A):
    left = 0
    right = len(A) - 1
    while left <= right:
        pivot = partition(A, left, right)
        if pivot == k - 1:
            return A[pivot]
        elif pivot < k - 1:
            left = pivot + 1
        else:
            right = pivot - 1


def partition(A, left, right):
    pivot_idx = random.randint(left, right)
    pivot_val = A[pivot_idx]
    new_pivot = left
    A[pivot_idx], A[right] = A[right], A[pivot_idx]
    for i in range(left, right):
        if A[i] > pivot_val:
            A[i], A[new_pivot] = A[new_pivot], A[i]
            new_pivot += 1
    A[right], A[new_pivot] = A[new_pivot], A[right]
    return new_pivot
```

## Explanation
* Select an element at random (the pivot), and partition the rest of the elements into those greater than the pivot and less than the pivot
    1. If there are exactly _k_ - 1 elements > pivot:
        * The pivot is the *k*th largest element
    2. If there are more than _k_ - 1 elements > pivot:
        * The *k*th largest element > pivot
        * Discard elements <= pivot
    3. If there are less than _k_ - 1 elements > pivot:
        * Discard elements >= pivot
* The `partition()` function is an implementation of the [Lomuto partition scheme](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)

## Code Dissection - find_kth_largest
1. Set a left and right pointer at the start and end of the array respectively
    ```python
    left = 0
    right = len(A) - 1
    ```
2. Loop until the left and right pointer meet each other
    ```python
    while left < right:
    ```
3. Partition array around random pivot and get the new index of the pivot
    ```python
    pivot = partition(A, left, right)
    ```
4. Check if the pivot is the *k*th largest element
    ```python
    if pivot == k - 1:
        return A[pivot]
    elif pivot < k - 1:
        left = pivot + 1
    else:
        right = pivot - 1
    ```

## Code Dissection - partition
1. Generate a random pivot index between _left_ and _right_
    ```python
    pivot_idx = random.randint(left, right)
    ```
2. Partition _A_[_left_ : _right_+1] around _pivot_
    ```python
    pivot_val = A[pivot_idx]
    new_pivot = left
    A[pivot_idx], A[right] = A[right], A[pivot_idx]
    for i in range(left, right):
        if A[i] > pivot_val:
            A[i], A[new_pivot] = A[new_pivot], A[i]
            new_pivot += 1
    A[right], A[new_pivot] = A[new_pivot], A[right]
    ```
    * After this process:
        1. _A_[_left_ : *new_pivot*] contains elements > pivot
        2. _A_[*new_pivot*+1 : _right_+1] contains elements < pivot
3. Return the new pivot index
    ```python
    return new_pivot
    ```