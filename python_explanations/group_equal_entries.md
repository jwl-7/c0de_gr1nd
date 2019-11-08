# Partitioning and Sorting an Array with Many Repeated Entries
Given an array of people with ages/names, arrange the elements so that equal ages appear together.

## Example
```
 Input: [[2, 'Bob'], [1, 'Joe'], [3, 'John'], [2, 'Alice'], [4, 'Frank'], [1, 'Sally'], [4, 'Sam']]
Output: [[1, 'Sally'], [1, 'Joe'], [2, 'Bob'], [2, 'Alice'], [3, 'John'], [4, 'Frank'], [4, 'Sam']]
```

## Solution
```python
Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people):
    people.sort(key=lambda x: x.age)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK