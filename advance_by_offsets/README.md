# Advancing Through an Array     
  
Problem:  
Write a program which takes an array of n integers, where A[i] denotes the maximum you can advance from index i, and returns whether it is possible to advance to the last index starting from the beginning of the array.    
    
Examples:  
```  
[3, 3, 1, 0, 2, 0, 1] = True, a valid advance sequence is: 0 -> 1 -> 4 -> 6 -> 6
[3, 2, 0, 0, 2, 0, 1] = False
```  
    
Solution - from [advance-by-offsets-mysol.py](advance-by-offsets-mysol.py):  
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
  
Explanation:  
  
The solution takes the approach of trying to advance as far as index i allows, while taking into account the other indexes along the way without backtracking.  
  
1. Set 3 variables that are used to iterate through the array:  
    ```python
    furthest = 0
    end = len(A) - 1
    i = 0
    ```  
    i signifies