# Generate Nonuniform Random Numbers
Given a random number generator that returns 0 or 1, generate one of the numbers in the given numbers array with the given probabilities.

## Example
```
values = [0, 1, 2, 3, 4]
probabilities = [0.05, 0.15, 0.3, 0.4, 0.6]

Output1: 3
Output2: 2
Output3: 0
Output4: 3
Output6: 2
Output7: 3
Output8: 3
Output9: 4
```

## Solution
```python
def nonuniform_random_number_generation(values, probabilities):
    intervals = list(itertools.accumulate(probabilities))
    r_num = random.random()
    for i in range(len(intervals)):
        if r_num <= intervals[i]:
            return values[i]
```

## Explanation
Let's use the example above to make sense of this problem:
```
values = [0, 1, 2, 3, 4]
probabilities = [0.05, 0.15, 0.3, 0.4, 0.6]
```
* The intervals from the probabilites are created using _p_<sub>0</sub>, _p_<sub>0</sub> + _p_<sub>1</sub>, _p_<sub>0</sub> + _p_<sub>1</sub> + _p_<sub>2</sub>, ... , _p_<sub>_n_ - 1</sub>
* Given these probabilities, they create the intervals:
    `[0.05, 0.2), [0.2, 0.5), [0.5, 0.9), [0.9, 1.5)`
* In the solution, the intervals are represented as an array of the same length as the values and probabilities:
    `[0.05, 0.2, 0.5, 0.9, 1.5]`
* Using a random number generator, we create a floating point number in [0, 1)
* For example, let's say the random number generated is 0.377877; it would fit in the interval [0.2, 0.5)
* The number 0.377877 corresponds to 0.5 (intervals[2]), which corresponds to 2 (values[2])
* Thus, the nonuniform random number returned would be 2

## Code Dissection
1. Use `itertools.accumulate(iterable[, func])` to return a list of accumulated sums of the probabilities array &mdash; this will be our list of intervals
    ```python
    intervals = list(itertools.accumulate(probabilities))
    ```
2. Generate a random number in the interval [0, 1)
    ```python
    r_num = random.random()
    ```
3. Loop over _intervals_, find what interval the random number generated corresponds to, then return the value that the interval corresponds to
    ```python
    for i in range(len(intervals)):
        if r_num <= intervals[i]:
            return values[i]
    ```