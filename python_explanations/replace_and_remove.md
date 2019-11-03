# Replace and Remove
Given an array of characters, replace each 'a' with 2 'd's, and delete each 'b'. The given size specifies how many entries should be processed.

## Examples
```
Before: ['d', 'b', 'c', '', '', '']
 After: ['d', 'c']

Before: ['a', 'b', 'c', 'a', '', '', '', '']
 After: ['d', 'd', 'c', 'd', 'd']
```

## Pythonic Solution
```python
def replace_and_remove(size, s):
    s[:] = [x for y in s for x in (['d', 'd'] if y == 'a' else [y]) if x not in ['b', '']]
```

## Explanation
* The solution uses list comprehension to remove and replace items in the list
* Note that when using lists, the difference between `s[:] = b` and `s = b` is that the latter will not replace elements in the original list _s_

## Pythonic Code Dissection
1. Use list comprehension to replace each 'a' with two 'd's and remove each 'b' and empty entry ''
    ```python
    def replace_and_remove(size, s):
        s[:] = [x for y in s for x in (['d', 'd'] if y == 'a' else [y]) if x not in ['b', '']]
    ```
    1. To understand this somewhat overly complicated one-line statement, let's separate it into two equivalent statements
        ```python
        s[:] = [x for y in s for x in (['d', 'd'] if y == 'a' else [y])]
        s[:] = [x for x in s if x not in ['b', '']]
        ```
    2. Now we can clearly see the two statements for removing and replacing characters, but let's separate them into multiple lines for arguably more readability
        ```python
        s[:] = [
            x
            for y in s
            for x in (['d', 'd']
                if y == 'a'
                else [y])
        ]

        s[:] = [
            x
            for x in s
            if x not in ['b', '']
        ]
        ```
    3. And here are some equivalent, inefficient statements that are easy to understand
        ```python
        for index, char in enumerate(s):
            if char == 'a':
                s[index:index + 1] = 'dd'
        for char in s[:]:
            if char in ['b', '']:
                s.remove(char)
        ```