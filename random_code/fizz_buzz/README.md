# Fizz Buzz
Write a program that outputs the string representation of numbers from 1 to n.

For each multiple of 3, print 'Fizz' instead of the number.\
For each multiple of 5, print 'Buzz' instead of the number.\
For numbers which are multiples of both 3 and 5, print 'FizzBuzz' instead of the number.

## Example
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

## Solution
```python
class Solution:
    def fizzy(self, n):
        list = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                list.append('FizzBuzz')
            elif i % 3 == 0:
                list.append('Fizz')
            elif i % 5 == 0:
                list.append('Buzz')
            else:
                list.append(str(i))
        return '\n'.join(list)
```

## Explanation
* The modulo operator finds the remainder after the division of one number by another

## Code Dissection
1. Create a list that will store the output of numbers 1 to _n_, then create a loop to iterate over those numbers
    ```python
    list = []
    for i in range(1, n + 1):
    ```
2. If the number is divisible by both 3 and 5, add 'FizzBuzz' to the list
    ```python
    if i % 15 == 0:
        list.append('FizzBuzz')
    ```
3. If the number is divisible by 3, add 'Fizz' to the list
    ```python
    elif i % 3 == 0:
        list.append('Fizz')
    ```
4. If the number is divisible by 5, add 'Buzz' to the list
    ```python
    elif i % 5 == 0:
        list.append('Buzz')
    ```
5. If the number is not divisible by 3 and 5, add the number to the list
    ```python
    else:
        list.append(str(i))
    ```
6. Return the list
    ```python
    return '\n'.join(list)
    ```