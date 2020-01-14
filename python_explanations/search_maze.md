# Search a Maze
Given a maze represented by a binary matrix, determine if it is possible to navigate from the given start coordinates to the given end coordinates. 1's represent closed walls, and 0's represent open paths. Return the path from start to end if navigation is possible.

## Examples
```
 Input: maze = [[0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]]
        start = [2, 2]
        end   = [1, 4]
Output: [Coordinate(x=2, y=2), Coordinate(x=1, y=2), Coordinate(x=1, y=1),
         Coordinate(x=2, y=1), Coordinate(x=3, y=1), Coordinate(x=4, y=1),
         Coordinate(x=5, y=1), Coordinate(x=6, y=1), Coordinate(x=6, y=2),
         Coordinate(x=5, y=2), Coordinate(x=4, y=2), Coordinate(x=3, y=2),
         Coordinate(x=3, y=3), Coordinate(x=2, y=3), Coordinate(x=1, y=3),
         Coordinate(x=1, y=4)]

The maze can be navigated from start to end.


 Input: maze = [[0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0]]
        start = [3, 1]
        end   = [0, 4]
Output: []

The maze cannot be navigated from start to end.
```

## Solution
```python
Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, start, end):
    def dfs(curr):
        if not (
            0 <= curr.x < len(maze) and
            0 <= curr.y < len(maze[curr.x]) and
            maze[curr.x][curr.y] == 0
        ):
            return False

        path.append(curr)
        maze[curr.x][curr.y] = 1

        if curr == end:
            return True

        moves = map(Coordinate,
                    (curr.x - 1, curr.x + 1, curr.x, curr.x),
                    (curr.y, curr.y, curr.y - 1, curr.y + 1))

        if any(map(dfs, moves)):
            return True

        del path[-1]
        return False

    path = []
    dfs(start)
    return path
```

## Explanation
* BLANK

## Code Dissection - search_maze
1. BLANK

## Code Dissection - dfs
1. BLANK