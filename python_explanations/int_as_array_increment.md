# Increment an Arbitrary-Precision Integer
Write a program that takes as input an array of digits encoding a nonnegative decimal integer _D_ and updates the array to represent the integer _D_ &plus; 1.

## Examples
```
[1, 2, 9] -> [1, 3, 0]
[9, 9, 9, 9] -> [1, 0, 0, 0, 0]
[1, 2, 3, 4, 5, 6, 7, 8, 9] -> [1, 2, 3, 4, 5, 6, 7, 9, 0]
```

## Solution
```python
def plus_one(A):
    for i in reversed(range(len(A))):
        A[i] += 1
        if A[i] < 10:
            break
        elif A[i] == A[0]:
            A[0] = 1
            A.append(0)
        else:
            A[i] = 0
    return A
```

## Explanation
* The solution uses the grade-school algorithm for adding integers, which is to add the digits from right to left, and carry when necessary

## Code Dissection
1. Iterate through _A_ from [right -> left]
    ```python
    for i in reversed(range(len(A))):
    ```
2. Increment _A_[_i_]; if the result is less than 10, there is no carry, so break out of the loop
    ```python
    A[i] += 1
    if A[i] < 10:
        break
    ```
3. If _A_[_i_] is the first index of _A_, carry in 1, and add 0 to the end of _A_
    ```python
    elif A[i] == A[0]:
        A[0] = 1
        A.append(0)
    ```
4. If _A_[_i_] is greater than 10 and not the first index of _A_, set _A_[_i_] to 0
    ```python
    else:
        A[i] = 0
    ```
    * The carry-out will be added in the next loop iteration
5. Return the incremented arbitrary-precision integer
    ```python
    return A
    ```

## Step-by-Step Example
* Let _A_ = [9, 9, 9, 9]
```
A = [9, 9, 9, 9]     (initial value)
A = [9, 9, 9, 0]     (carry-out = 1)
A = [9, 9, 0, 0]     (carry-in = 1, carry-out = 1)
A = [9, 0, 0, 0]     (carry-in = 1, carry-out = 1)
A = [1, 0, 0, 0, 0]  (carry-in = 1, carry-out = 1)

Notice that because the loop reached A[0] and
the digit with the carry-in > 10, A[0] was set to 1, and
a zero was appended to the end of A

The array returned is A = [1, 0, 0, 0, 0]
```