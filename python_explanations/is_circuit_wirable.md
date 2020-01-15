# Making Wired Connections
BLANK

## Example
```
0----1
|    |
|    |
3----2

 Input: [[0, 2], [1, 3], [3, 1], [2, 0]]
Output: True

The vertices can be divided into the two groups: {0, 2} and {1, 3}
```

## Solution
```python
def is_any_placement_feasible(graph):
    def bfs(s):
        s.color = 0
        q = collections.deque([s])
        while q:
            curr = q.popleft()
            for v in curr.edges:
                if v.color == -1:
                    v.color = curr.color + 1
                    q.append(v)
                elif v.color == curr.color:
                    return False
        return True

    return all(bfs(v) for v in graph if v.color == -1)
```

## Explanation
* BLANK

## Code Dissection - is_any_placement_feasible
1. BLANK

## Code Dissection - bfs
1. BLANK