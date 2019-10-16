# The Look-and-Say Problem
The look-and-say sequence starts with 1. Subsequent numbers are derived by describing the previous number in terms of consecutive digits. Specifically, to generate an entry of the sequence from the previous entry, read off the digits of the previous entry, counting the number of digits in groups of the same digit. For example, 1; one 1; two 1s; one 2 then one 1; one 1, then one 2, then two 1s; three 1s, then two 2s, then one 1. The first eight numbers in the look-and-say sequence are {1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211}

Write a program that takes as input an integer _n_ and returns the *n*th integer in the look-and-say sequence. Return the result as a string.

## Examples
```
 Input: 4
Output: '1211'

 Input: 7
Output: '13112221'
```

## Solution
```python
def look_and_say(n):
    s = '1'
    for _ in range(1, n):
        tmp = ''
        prev = s[0]
        count = 0
        for char in s:
            if prev == char:
                count += 1
            else:
                tmp += str(count) + prev
                prev = char
                count = 1
        tmp += str(count) + char
        s = tmp
    return s
```

## Explanation
* Since each entry in the sequence builds off the previous, it only makes sense to build each entry up to _n_
* The first loop is used to generate each entry up to _n_, while the second loop is used to process the previous entry

## Code Dissection
1. Initialize a result variable to the first entry in the sequence which is '1'
    ```python
    s = '1'
    ```
2. Create an outer loop that runs from 1 to _n_, rather than just to _n_, since the first entry is already defined
    ```python
    for _ in range(1, n):
        tmp = ''
        prev = s[0]
        count = 0
    ```
    * This loop is used to generate each entry up to _n_
    * We use ```for _```, since the loop iteration variable is not used
    * ```tmp``` is used to hold each entry
    * ```prev``` is used to compare characters
    * ```count``` is used to store the consecutive matches between _prev_ and _char_
3. Create an inner loop that iterates through each character in _s_
    ```python
    for char in s:
    ```
    * This loop is used to process the previous entry in the sequence
4. Increment the counter if _char_ matches _prev_
    ```python
    if prev == char:
        count += 1
    ```
5. Otherwise, add the match count and digit we just processed to _tmp_ and then set _prev_ to the current digit
    ```python
    else:
        tmp += str(count) + prev
        prev = char
        count = 1
    ```
6. Add to _tmp_ one last time when breaking out of the inner loop, and then set _s_ to _tmp_ so that the outer loop can process the entry
    ```python
    tmp += str(count) + char
    s = tmp
    ```
7. Return the *n*th entry in the sequence
    ```python
    return s
    ```