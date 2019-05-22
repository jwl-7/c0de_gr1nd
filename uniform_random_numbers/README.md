# Generate Uniform Random Numbers  

"This problem is motivated by the following scenario. Six friends have to select a designated driver using a single unbiased coin. The process should be fair to everyone." - EPI  
  
Problem:  
How would you implement a random number generator that generates a random integer i between a and b, inclusive, given a random number generator that produces zero or one with equal probability? All values in [a,b] should be equally likely.  
  
Examples:  
```
 Input: [1, 6]
Output: 1
Output: 5
Output: 2
  
 Input: [0, 10]
Output: 9
Output: 8
Output: 10
```  
  
Solution - from [uniform-random-number-mysol.py](uniform-random-number-mysol.py):  
```python
def zero_one_random():
    return random.randrange(2)

def uniform_random(lower_bound, upper_bound):
    p = upper_bound - lower_bound + 1
    while True:
        num = 0
        i = 0
        while 1 << i < p:
            num = num << 1 | zero_one_random()
            i += 1
        if num < p:
            break
    return num  
```  
  
Explanation: 
  
The solution is based on [Rejection Sampling](https://en.wikipedia.org/wiki/Rejection_sampling). This basically means that if the number generated is not within the desired range, then resample the number.  
  
1. The given function is a number generator that produces 0 or 1 with equal probability  
    ```python
    def zero_one_random():
        return random.randrange(2)
    ```  
2. Set a variable with the range (p) using the given lower_bound and upper_bound  
    ```python
    p = upper_bound - lower_bound + 1
    ```  
   The reason + 1 is added to p, is because the stopping point of a random range is excluded from the range. For instance, if you wanted to generate a random number for a dice roll [1, 6], the number 6 should be included in the range.  
3. Loop until a uniform random number is generated  
4. Initialize the random number (num) and the resample loop counter (i) = 0  
    ```python
    num = 0
    i = 0
    ```    
6. Loop until i * 2 is out of the desired range (p)  
    ```python
    while 1 << i < p:
    ```  
    a. Generate a random number (num) with the help of the given random number generator and increase the loop counter (i)  
    ```python
    num = num << 1 | zero_one_random()
    i += 1
    ```  
7. If the random number (num) is within the desired range (p), break out of the resample loop  
    ```python
    if num < p:
        break
    ```  
8. Return the uniform random number  
  
</br>  
  
[Python Bitwise Operators Reference](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)