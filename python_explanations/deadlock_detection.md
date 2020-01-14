# Deadlock Detection
Given a directed graph, determine whether or not it contains a cycle.

## Examples
<img src='drawio_diagrams/deadlock_detection1.svg' width='40%'>

```
 Input: [[0, 1], [1, 2], [2, 0]]
Output: True
```

<img src='drawio_diagrams/deadlock_detection2.svg' width='50%'>

```
 Input: [[0, 1], [1, 2], [2, 3]]
Output: False
```

## Solution
```python
def is_deadlocked(graph):
    def has_cycle(curr):
        if curr.color == GraphVertex.GRAY:
            return True

        curr.color = GraphVertex.GRAY

        for nxt in curr.edges:
            if nxt.color != GraphVertex.BLACK and has_cycle(nxt):
                return True

        curr.color = GraphVertex.BLACK
        return False

    for vertex in graph:
        if vertex.color == GraphVertex.WHITE and has_cycle(vertex):
            return True
    return False
```

## Explanation
* BLANK

## Code Dissection
1. BLANK