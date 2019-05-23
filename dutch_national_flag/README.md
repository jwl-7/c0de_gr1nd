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
    return A
```  
  
Explanation:  
  
The solution uses an efficient [quicksort](https://opendatastructures.org/ods-python/11_1_Comparison_Based_Sorti.html#49745) algorithm.  
   
1. Set the variables for the pivot point and 3 pointers used to iterate through the array and swap the elements  
    ```python
    pivot = A[pivot_index]
    low = 0
    mid = 0
    high = len(A) - 1
    ```  
2. Loop until the mid pointer passes the high pointer  
3. If the mid pointer < pivot, swap Array[mid] and Array[low], and decrease the low and mid pointers  
    ```python
    if A[mid] < pivot:
    A[mid], A[low] = A[low], A[mid]
    low += 1
    mid += 1
    ```  
4. If the mid pointer == pivot, don't swap anything, and increase the mid pointer  
    ```python
    elif A[mid] == pivot:
    mid += 1
    ```  
5. If the mid pointer > pivot, swap Array[mid] and Array[high], and decrease the high pointer  
    ```python
    elif A[mid] > pivot:
    A[mid], A[high] = A[high], A[mid]
    high -= 1
    ```  
6. Return the partitioned array  
  
</br>  
  
Example if the Array = [1, 1, 0, 2] and the Pivot Index = 1:    
  
|low, mid|   |   |high|
|-------:|---|---|----|
|      1 | 1 | 0 | 2  |  

| low| mid |   |high|
|---:|:---:|---|----|
|  1 |  1  | 0 | 2  |  

| low|   | mid |high|
|---:|---|:---:|----|
|  1 | 1 |  0  | 2  |  

|     | low |     |mid, high|
|-----|:---:|-----|---------|
|**0**|  1  |**1**| 2       |  

|   | low | high |   |mid|
|---|:---:|:----:|---|---|
| 0 |  1  |  1   | 2 |   |  