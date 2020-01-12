# Schedule to Minimize Waiting Time
Given the processing times for a set of SQL queries, schedule the queries for the minimum total waiting time.

## Examples
```
 Input: [3, 1, 2, 4]
Output: 10

 Input: [7, 3, 7, 3, 3, 1]
Output: 39
```

## Solution
```python
def minimum_total_waiting_time(service_times):
    n = len(service_times)
    service_times.sort()
    total_time = 0
    for i, time in enumerate(service_times):
        queries = n - (i + 1)
        total_time += time * queries
    return total_time
```

## Explanation
* BLANK

## Code Dissection
1. BLANK