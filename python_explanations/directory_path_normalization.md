# Normalize Pathnames
A file or directory can be specified via a string called the pathname. This string may specify an absolute path, starting from the root, e.g., /usr/bin/gcc, or a path relative to the current working directory, e.g., scripts/awkscripts.

The same directory may be specified by multiple directory paths. For example, /usr/lib/../bin/gcc and scripts//./../scripts/awkscripts/././ specify equivalent absolute and relative pathnames.

Write a program which takes a pathname, and returns the shortest equivalent pathname. Assume individual directories and files have names that use only alphanumeric characters. Subdirectory names may be combined using forward slashes (/), the current directory (.), and parent directory (..).

## Examples
```
 Input: usr/lib/../bin/gcc
Output: usr/bin/gcc

 Input: rXkau/../../..
Output: ../..

 Input: ///
Output: /
```

## Solution
```python
def shortest_equivalent_path(path):
    stack = []
    for p in path.split('/'):
        if p == '..':
            if not stack or stack[-1] == '..':
                stack.append(p)
            else:
                stack.pop()
        elif p and p != '.':
            stack.append(p)
    return ('/' if path[0] == '/' else '') + '/'.join(stack)
```

## Explanation
* Note that the problem is referring to pathnames in a UNIX-style file system
* Keep in mind what the special characters in the pathnames mean:
    * `.` = current directory
    * `..` = parent directory (one directory up)
    * If pathname starts with `/`, then we cannot go up from it

The solution uses the following algorithm:
1. The path is split on the delimeter '/'
2. The special characters that may be in the path are '.', '..', or ''
3. '' occurs when the path contains '//'
4. '.' and '' are ignored
5. For '..':
    1. If the stack is not empty, pop from the stack
    2. If the stack is empty or the top of the stack is '..', push to the stack
6. For other parts of the path, push to the stack
7. Return each part of the stack separated by '/', and if the path started with '/', then make sure to add that to the front of the result

## Code Dissection
1. Create an empty stack to help build the pathname
    ```python
    stack = []
    ```
2. Loop over each part of the path separated by '/'
    ```python
    for p in path.split('/'):
    ```
3. If the part is '..', push it to the stack if the stack is empty or the top is '..', else pop from the stack
    ```python
    if p == '..':
        if not stack or stack[-1] == '..':
            stack.append(p)
        else:
            stack.pop()
    ```
4. If the part is not '' and not '.', push it to the stack
    ```python
    elif p and p != '.':
        stack.append(p)
    ```
5. Return each part of the stack joined by '/', and add '/' to the front if the original path started like that
    ```python
    return ('/' if path[0] == '/' else '') + '/'.join(stack)
    ```