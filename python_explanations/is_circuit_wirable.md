# Making Wired Connections
Given a set of pins and a set of wires, determine if the pins can be placed on the left and right side of the PCB such that each wire is between each side.

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
* The question is asking to determine if the graph is bipartite
* A graph is bipartite if we can divide the vertices into two independent subsets _A_ and _B_ such that every edge connects a vertex in _A_ to a vertex in _B_
* Perform a BFS and make sure that every edge connects vertices of different colors:
    * -1 = no color
    * 0 = red
    * 1 = green

## Code Dissection - is_any_placement_feasible
1. Run `bfs()` to visit all the vertices, and check if any edge connects two vertices of the same color
    ```python
    return all(bfs(v) for v in graph if v.color == -1)
    ```
    * The graph is bipartite if every edge connects from a red vertex to a green vertex

## Code Dissection - bfs
1. Set the vertex color to red (0) on visit and use it as the starting point for the BFS
    ```python
    s.color = 0
    q = collections.deque([s])
    ```
2. From the starting vertex (_s_), find its neighbors and set the connected vertices to the other color
    ```python
    while q:
        curr = q.popleft()
        for v in curr.edges:
            if v.color == -1:
                v.color = curr.color + 1
                q.append(v)
    ```
3. If we try to connect to a vertex of the same color, then return False
    ```python
    elif v.color == curr.color:
        return False
    ```
4. If all the edges in the search get connected from a red vertex to a green vertex, then return True
    ```python
    return True
    ```