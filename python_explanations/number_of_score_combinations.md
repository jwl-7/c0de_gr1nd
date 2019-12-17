# Count the Number of Score Combinations
Given the final score in a football game and a list of scores for individual plays, compute the number of score combinations.

Football plays:
* 2 points - safety
* 3 points - field goal
* 7 points - touchdown

## Examples
```
 Input: final score = 12
        play scores = [2, 3, 7]
Output: 4

 Input: final score = 88
        play scores = [79, 59, 4, 114, 53, 44]
Output: 3
```

## Solution
```python
def num_combinations_for_final_score(final_score, play_scores):
    dp = [[1] + [0] * final_score for _ in play_scores]
    for i in range(1, final_score + 1):
        for j in range(len(play_scores)):
            x = dp[j-1][i]
            y = dp[j][i - play_scores[j]] if i >= play_scores[j] else 0
            dp[j][i] = x + y
    return dp[-1][-1]
```

## Explanation
* The idea is to create a DP table the size of *play_scores* (rows) * *final_score* (columns) to store counts of all scores from 0 to *final_score*
* Compute the number of combinations for each possible number of plays of each type

## Code Dissection
1. Create a DP table to store counts of all scores from 0 to *final_score*
    ```python
    dp = [[1] + [0] * final_score for _ in play_scores]
    ```
2. Outer loop: loop over the final scores in the table (columns)
    ```python
    for i in range(1, final_score + 1):
    ```
3. Inner loop: loop over the play scores in the table (rows)
    ```python
    for j in range(len(play_scores)):
    ```
4. Count the number of combinations excluding play_scores[_j_]
    ```python
    x = dp[j-1][i]
    ```
5. Count the number of combinations including play_scores[_j_]
    ```python
    y = dp[j][i - play_scores[j]] if i >= play_scores[j] else 0
    ```
6. Add the total number of combinations to the DP table
    ```python
    dp[j][i] = x + y
    ```
7. Return the final count from the DP table &mdash; total number of score combinations
    ```python
    return dp[-1][-1]
    ```