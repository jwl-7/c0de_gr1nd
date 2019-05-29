# Delete Duplicates from a Sorted Array  
  
Problem:  
Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the remaining elements have been shifted left to fill the emptied indices. Return the number of valid elements. Many languages have library functions for performing this operation -- you cannot use these functions.  
    
Examples:  
```  
  Input: [-1, -1, 0, 1, 1, 2, 2, 3]
Updated: [-1, 0, 1, 2, 3, 2, 2, 3]
  Valid: [-1, 0, 1, 2, 3]
 Output: 5

  Input: [2, 3, 5, 5, 7, 11, 11, 11, 13]
Updated: [2, 3, 5, 7, 11, 13, 11, 11, 13]
  Valid: [2, 3, 5, 7, 11, 13]
 Output: 6

  Input: [-4, -3, -3, -2, -1, 0, 1, 2, 2, 3, 3, 4, 5, 5]
Updated: [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 3, 4, 5, 5]
  Valid: [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
 Output: 10
```  
    
Solution - from [sorted-array-remove-dups-mysol.py](sorted-array-remove-dups-mysol.py):  
```python
def delete_duplicates(A):
    valid = 0
    for i in range(1, len(A)):
        if A[valid] != A[i]:
            valid += 1
            A[valid] = A[i]
    return valid + 1
```    
  
Explanation:  
  
1. Since the array is already sorted, we can use two pointers to iterate through the array and identify duplicates:  
    ```python
    valid = 0
    for i in range(1, len(A)):
    ```  
    -- valid -> starts at index[0], also keeps track of number of valid entries  
    -- i -> starts at index[1]  
2. If A[valid] != A[i], there is no duplicate, and A[i] is copied into A[valid + 1]  
    ```python
    if A[valid] != A[i]:
        valid += 1
        A[valid] = A[i]
    ```  
3. Return the number of valid elements  
    ```python
    return valid + 1
    ```  
    -- 1 is added to valid, since the count originally started at 0 (for array index purposes)  