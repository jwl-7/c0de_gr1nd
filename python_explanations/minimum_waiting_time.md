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
* The idea is to perform the queries with the shortest service times first

## Code Dissection
1. Get the number of queries, sort them, then initialize the total waiting time to zero
    ```python
    n = len(service_times)
    service_times.sort()
    total_time = 0
    ```
2. Loop through each query
    ```python
    for i, time in enumerate(service_times):
    ```
3. Calculate the number of queries left to the process
    ```python
    queries = n - (i + 1)
    ```
4. Add the current query service time * number of remaining queries to the total waiting time
    ```python
    total_time += time * queries
    ```
5. Return the minimal waiting time
    ```python
    return total_time
    ```