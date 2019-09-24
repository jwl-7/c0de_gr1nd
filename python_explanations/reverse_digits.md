# Reverse Digits
Write a program which takes an integer and returns the integer corresponding to the digits of the input written in reverse order.  
  
## Examples
```
42 -> 24
-94 -> -49
-314 -> -413
2117 -> 7112
```
  
## Solution
```python
def reverse(x):
    r = 0
    temp = abs(x)
    while temp:
        r = r * 10 + temp % 10
        temp //= 10
    return -r if x < 0 else r
```
  
## Pythonic Solution
```python
def reverse(x):
    return -int(str(abs(x))[::-1]) if x < 0 else int(str(x)[::-1])
```
  
## Explanation
* The solution uses some relatively simple arithmetic to perform 3 key steps to build the reversed number:
    1. Extract the last digit in the number
    2. Append the extracted digit to the reversed number
    3. Remove the last digit from the number
* The pythonic solution uses slice notation to reverse a string representation of the number and then convert it back to an integer
* Both solutions have similar performance, but the pythonic solution has a more consistent runtime
  
## Code Dissection
1. Create a variable to hold the reversed number and a temporary variable to hold the absolute value of the number
    ```python
    r = 0
    temp = abs(x)
    ```
2. Loop until the temporary variable is empty, which will be the case when we have computed the reversed number
    ```python
    while temp:
    ```
    * ```while temp``` is equivalent to ```while temp == 0``` in this case, because temp will always equal zero by the end of this operation
3. Extract the last digit from _temp_ and append it to the reversed number
    ```python
    r = r * 10 + temp % 10
    ```
4. Remove the last digit from _temp_
    ```python
    temp //= 10
    ```
5. Return the reversed number with the correct sign
    ```python
    return -r if x < 0 else r
    ```
  
## Pythonic Code Dissection
1. Use built-in functions to convert the number to a string, use slice notation to reverse the number string, convert the reversed number string back to an integer, and then return the reversed number
    ```python
    return -int(str(abs(x))[::-1]) if x < 0 else int(str(x)[::-1])
    ```
    Let's separate this mushed one-liner into multiple lines for easier readability:
    ```python
    if x < 0:
        return -int(str(abs(x))[::-1])
    else:
        return int(str(x)[::-1])
    ```
    * Now we can clearly see there are two cases: 1 for negative numbers and 1 for positive numbers
    * ```abs(x)``` returns the absolute value of _x_
    * ```str(x)[::-1]``` converts _x_ into a string and reverses it using slice notation
    * ```int(str(x))``` converts the reversed string back into an integer