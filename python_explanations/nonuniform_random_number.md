# Generate Nonuniform Random Numbers
You are given _n_ numbers as well as probabilities _p_<sub>0</sub>, _p_<sub>1</sub>, ... , _p_ <sub>_n_-1</sub>, which sum up to 1. Given a random number generator that produces values in [0, 1) uniformly, how would you generate one of the _n_ numbers according to the specified probabilities?  
  
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
* BLANK  
  
## Code Dissection
1. BLANK  