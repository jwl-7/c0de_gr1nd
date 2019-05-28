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
  
The solution takes the approach of trying to advance as far as index i allows, while iterating through all entries in A.   
  
1. Set 3 variables that are used to advance through the array:  
    ```python
    furthest = 0
    end = len(A) - 1
    i = 0
    ```  
    -- furthest is used to store the furthest index reached  
    -- end represents the last index of the array  
    -- i is used to iterate through the array  
2. Loop while the current index is before the furthest reached and the furthest index reached is before the end  
    ```python
    while i <= furthest and furthest < end:
    ```  
3. Iterate through each entry in the array and track the furthest index that can be reached  
    ```python
    furthest = max(furthest, A[i] + i)
    i += 1
    ```  
    -- The furthest index i that can be reached from the current index i = A[i] + i  
4. Return whether or not it is possible to advance to the end of the array  
    ```python
    return furthest >= end
    ```  
    If the furthest index reached >= the last index, then this statement will return True  
  
</br>  
  
Example if the Array = [3, 3, 1, 0, 2, 0, 1]  
   
Let i = current index and f = furthest index reached  
  
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