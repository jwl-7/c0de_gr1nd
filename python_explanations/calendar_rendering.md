# Render a Calendar
Given a set of events, find the maximum number of events that can happen at the same time.

## Example
```
 Input: [[1, 5], [2, 7], [4, 5], [6, 10], [8, 9], [9, 17], [11, 13], [12, 15], [14, 15], [9, 10]]
Output: 4
```

## Solution
```python
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    endpoints = [
        x for event in A for x in (
            Endpoint(event.start, True),
            Endpoint(event.finish, False)
        )
    ]
    endpoints.sort(key=lambda x: (x.time, not x.is_start))
    max_events = 0
    num_events = 0
    for event in endpoints:
        if event.is_start:
            num_events += 1
            max_events = max(num_events, max_events)
        else:
            num_events -= 1
    return max_events
```

## Explanation
* BLANK

## Code Dissection
1. BLANK