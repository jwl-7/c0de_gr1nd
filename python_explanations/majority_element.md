# Find the Majority Element
Given a sequence of strings, find the string that occurs the most within one pass.

## Examples
```
 Input: ['2', '1', '2', '2', '2', '1', '2', '2']
Output: 2

 Input: ['4', '4', '4', '1', '4', '4', '3', '3']
Output: 4
```

## Solution
```python
def majority_search(stream):
    m = None
    m_count = 0
    for s in stream:
        if not m_count:
            m = s
            m_count += 1
        elif m == s:
            m_count += 1
        else:
            m_count -= 1
    return m
```

## Explanation
Starting with the first string _s_ as the candidate _m_ for the majority element:
    * If _m_ == _s_, increment the counter
    * If _m_ != _s_, decrement the counter
    * If the counter == 0, set the next string as _m_

## Code Dissection
1. Initialize the candidate for the majority element to None and its count to zero
    ```python
    m = None
    m_count = 0
    ```
2. Iterate through each string in the sequence
    ```python
    for s in stream:
    ```
3. If *m_count* == 0, set the next string as _m_
    ```python
    if not m_count:
        m = s
        m_count += 1
    ```
4. If _m_ == _s_, increment the counter, otherwise decrement
    ```python
    elif m == s:
        m_count += 1
    else:
        m_count -= 1
    ```
5. Return the majority element
    ```python
    return m
    ```