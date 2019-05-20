# Fizz Buzz

Problem:  
Write a program that outputs the string representation of numbers from 1 to n.   
For each multiple of 3, print 'Fizz' instead of the number.   
For each multiple of 5, print 'Buzz' instead of the number.   
For numbers which are multiples of both 3 and 5, print 'FizzBuzz' instead of the number.  
  
Example:  
```
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```  
  
Solution (from [fizzbuzz.py](fizzbuzz.py)): 
```python
def fizzy(n):
    list = []
    for i in range(1, n + 1):
        if i % 15 == 0: list.append('FizzBuzz')
        elif i % 3 == 0: list.append('Fizz')
        elif i % 5 == 0: list.append('Buzz')
        else: list.append(str(i))
    return '\n'.join(list)
```  
  
Explanation:  
1. Create a list that will hold the output of numbers 1 to n  
2. Loop over the numbers from 1 to n  
3. Use the % modulo operator to compute what the number is divisible by  
    a. If the number is divisible by both 3 and 5, add 'FizzBuzz' to the list  
    ```python
    if i % 15 == 0: list.append('FizzBuzz')
    ```
    b. Else if the number is divisible by both 3 and 5, add 'FizzBuzz' to the list  
    ```python
    elif i % 3 == 0: list.append('Fizz')
    ```
    c. Else if the number is divisible by both 3 and 5, add 'FizzBuzz' to the list  
    ```python
    elif i % 5 == 0: list.append('Buzz')
    ```
    d. Else, add the number to the list  
    ```python
    else: list.append(str(i))
    ```  
4. Return the list  