# Dutch National Flag Problem    
  
Problem:  
Write a program that takes an array A and an index i into A, and rearrange the elements such that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot, followed by elements greater than the pivot.    
    
Examples:  
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
    
Solution - from [dutch-national-flag-mysol.py](dutch-national-flag-mysol.py):  
```python
def dutch_flag_partition(pivot_index, A):
    # TODO - you fill in here.
    return
```  
  
Explanation:  
  
