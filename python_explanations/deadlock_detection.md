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
        if curr.color == GraphVertex.GREY:
            return True

        curr.color = GraphVertex.GREY

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
* Detect a cycle in a graph by using DFS that keeps track of vertices via colors
    * WHITE = vertex has not yet been visited (initial color)
    * GREY = vertex has been visited
    * BLACK = visited neighboring vertices and left the vertex
* Traverse the graph:
    * Process the vertex if color = WHITE
    * Ignore the vertex if color = BLACK
    * Graph contains cycle if color = GREY

## Code Dissection - is_deadlocked
1. Traverse the graph and look for a cycle
    ```python
    for vertex in graph:
        if vertex.color == GraphVertex.WHITE and has_cycle(vertex):
            return True
    return False
    ```

## Code Dissection - has_cycle
1. If we come across a grey vertex, then we have found a cycle (edge from grey vertex back to a grey vertex)
    ```python
    if curr.color == GraphVertex.GREY:
        return True
    ```
2. Set the vertex color to GREY on visit
    ```python
    curr.color = GraphVertex.GREY
    ```
3. Traverse the neighbor vertices
    ```python
    for nxt in curr.edges:
        if nxt.color != GraphVertex.BLACK and has_cycle(nxt):
            return True
    ```
4. After we finish processing a vertex, set the color to BLACK
    ```python
    curr.color = GraphVertex.BLACK
        return False
    ```