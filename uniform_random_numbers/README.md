# Generate Uniform Random Numbers  

"This problem is motivated by the following scenario. Six friends have to select a designated driver using a single unbiased coin. The process should be fair to everyone." - EPI  
  
Problem:  
How would you implement a random number generator that generates a random integer i between a and b, inclusive, given a random number generator that produces zero or one with equal probability? All values in [a,b] should be equally likely.  
  
Examples:  
```
 Input: [1, 6]
Output: 4
  
 Input: [1, 6]
Output: 3
  
 Input: [1, 6]
Output: 5
```  
  
Solution - from [uniform-random-number-mysol.py](uniform-random-number-mysol.py):  
```python
def zero_one_random():
    return random.randrange(2)

def uniform_random(lower_bound, upper_bound):
```  
  
Explanation:  
  
