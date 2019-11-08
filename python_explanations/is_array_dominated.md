# Team Photo Day&mdash;1
Given two teams and the heights of the players in the teams, determine if it's possible to get everyone in the photo.

## Examples
```
 Input: Team 0 - [1, 5, 4]
        Team 1 - [2, 3, 4]
Output: False
Conclusion: Team 0 cannot be placed in front of Team 1
            Team 1 cannot be placed in front of Team 0


 Input: Team 0 - [2, 3, 4]
        Team 1 - [0, 3, 2]
Output: True
Conclusion: Team 0 cannot be placed in front of Team 1
            Team 1 can be placed in front of Team 0
```

## Solution
```python
def valid_placement_exists(team0, team1):
    team0.players.sort()
    team1.players.sort()
    return all(x < y for x, y in zip(team0.players, team1.players))
```

## Explanation
1. Sort both teams' player heights
2. Compare the teams' player heights in pairs to check if Team 0 can stand in front of Team 1

## Code Dissection
1. Sort both teams' player heights
    ```python
    team0.players.sort()
    team1.players.sort()
    ```
2. Check if Team 0 can stand in front of Team 1
    ```python
    return all(x < y for x, y in zip(team0.players, team1.players))
    ```
    * `zip()` puts the player heights in pairs
    * `all()` will only return True if each comparison is True