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
* BLANK

## Code Dissection - clone_graph
1. BLANK

## Code Dissection - dfs
1. BLANK