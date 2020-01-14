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
* From the start position, try moving left, right, up, and down:
    * If we find an open path (0), add it to the solution path
    * If we find a closed path (1), ignore it and try the next move
* If the current solution path fails, backtrack

## Code Dissection - search_maze
1. Create empty solution path, run `dfs()`, and return the path
    ```python
    path = []
    dfs(start)
    return path
    ```

## Code Dissection - dfs
1. Check if current position is open (0) and in the maze
    ```python
    if not (
        0 <= curr.x < len(maze) and
        0 <= curr.y < len(maze[curr.x]) and
        maze[curr.x][curr.y] == 0
    ):
        return False
    ```
2. If the current position is valid, add it to the solution path
    ```python
    path.append(curr)
    ```
3. Mark the current cell as 1 to avoid repitition
    ```python
    maze[curr.x][curr.y] = 1
    ```
4. Stop the search if we have reached the end
    ```python
    if curr == end:
        return True
    ```
5. Map a set of coordinates for moving left, right, up, and down
    ```python
    moves = map(Coordinate,
                (curr.x - 1, curr.x + 1, curr.x, curr.x),
                (curr.y, curr.y, curr.y - 1, curr.y + 1))
    ```
6. Check if any of the possible moves work
    ```python
    if any(map(dfs, moves)):
        return True
    ```
7. Navigation failed, remove last coordinate in _path_ and backtrack
    ```python
    del path[-1]
    return False
    ```