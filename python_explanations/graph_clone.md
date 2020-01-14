# Clone a Graph
Given a reference to a vertex _u_ in a directed graph, return a deep copy of the graph. Each vertex contains an integer value and a list of its neighbors.

## Example
```
 Input: [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2]]
Output: [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2]]
```

## Solution
```python
def clone_graph(graph):
    def dfs(vertex):
        if vertex not in visited:
            copy = visited[vertex] = GraphVertex(vertex.label)
            copy.edges = map(dfs, vertex.edges)
        return visited[vertex]

    visited = {}
    return dfs(graph)
```

## Explanation
* Perform a DFS on the vertex _u_, using its list of neighbors to find vertices and a cache to keep track of visited ones

## Code Dissection - clone_graph
1. Create an empty cache and run `dfs()`
    ```python
    visited = {}
    return dfs(graph)
    ```

## Code Dissection - dfs
1. If the vertex is not in the cache, then add a copy of it
    ```python
    copy = visited[vertex] = GraphVertex(vertex.label)
    ```
2. Find the neighboring vertices
    ```python
    copy.edges = map(dfs, vertex.edges)
    ```
3. Return the copy of the vertex
    ```python
    return visited[vertex]
    ```