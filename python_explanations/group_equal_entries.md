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
* While the problem only asks for equal ages to be adjacent, any other sorting algorithm beyond something like a quicksort uses additional space complexity
* The book's solution uses 2 hash tables to maintain subarrays for different types of elements to swap elements around, which not only uses additional space but is way slower

## Code Dissection
1. Sort the array using the age as a key
    ```python
    people.sort(key=lambda x: x.age)
    ```