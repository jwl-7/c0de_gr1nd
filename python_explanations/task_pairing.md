# Compute an Optimum Assignment of Tasks
Given an array of task durations, assign the tasks to workers such that the work is completed in the minimum time possible. Each worker can be assigned two tasks.

## Examples
```
 Input: [3, 4, 2, 1]
Output: [[1, 4], [2, 3]]

 Input: [9, 2, 7, 10, 3, 0, 10, 7, 0, 3]
Output: [[0, 10], [0, 10], [2, 9], [3, 7], [3, 7]]
```

## Solution
```python
PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    task_durations.sort()
    return [
        PairedTasks(task_durations[i], task_durations[~i])
        for i in range(len(task_durations) // 2)
    ]
```

## Explanation
* BLANK

## Code Dissection
1. BLANK