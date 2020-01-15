# Team Photo Day&mdash;2
Given a set of teams and the heights of their players, determine the maximum number of teams that can be photographed at the same time with everyone in the photo.

## Examples
```
 Input: [[2, 7], [3, 6], [3, 4], [1, 5]]
Output: 2

 Input: [[0, 1], [3, 4], [0, 2], [0, 4], [2, 4], [2, 3], [1, 3], [1, 4], [1, 2], [0, 3]]
Output: 5
```

## Solution
```python
def find_largest_number_teams(graph):
    def dfs(s):
        s.max_distance = max(
            ((vertex.max_distance
                if vertex.max_distance != 0
                else dfs(vertex)) + 1
                for vertex in s.edges),
            default=1
        )
        return s.max_distance

    return max(dfs(v) for v in graph if v.max_distance == 0)
```

## Explanation
* The goal is to find a sequence of teams where a team can stand behind the one before it
* Form a DAG (Directed Acyclic Graph) with topological sorting, and find the longest valid path

## Code Dissection
1. BLANK