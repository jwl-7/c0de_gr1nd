# Replace and Remove
Write a program which takes as input an array of characters, and removes each 'b' and replaces each 'a' by two 'd's. Specifically, along with the array, you are provided an integer-valued size. Size denotes the number of entries of the array that the operation is to be applied to. You do not have to worry about preserving subsequent entries. For example, if the array is {_a_, _b_, _a_, _c_, _} and the size is 4, then you can return {_d_, _d_, _d_, _d_, _c_}. You can assume there is enough space in the array to hold the final result.
  
## Examples
```
Before: ['d', 'b', 'c', '', '', '']
 After: ['d', 'c']

Before: ['a', 'b', 'c', 'a', '', '', '', '']
 After: ['d', 'd', 'c', 'd', 'd']
```
  
## Solution
```python
def replace_and_remove(size, s):
    s[:] = [x for y in s for x in (['d', 'd'] if y == 'a' else [y])]
    s[:] = [x for x in s if x not in ['b', '']]
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK