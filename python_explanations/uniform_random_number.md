# Generate Uniform Random Numbers
This problem is motivated by the following scenario. Six friends have to select a designated driver using a single unbiased coin. The process should be fair to everyone.

How would you implement a random number generator that generates a random integer _i_ between _a_ and _b_, inclusive, given a random number generator that produces a zero or one with equal probability?

All values in [_a_, _b_] should be equally likely.

## Examples
```
 Input: [1, 6]
Output: 1
Output: 5
Output: 2

 Input: [0, 10]
Output: 9
Output: 8
Output: 10
```

## Solution
```python
def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound, upper_bound):
    p = upper_bound - lower_bound + 1
    while True:
        num = 0
        i = 0
        while 1 << i < p:
            num = num << 1 | zero_one_random()
            i += 1
        if num < p:
            break
    return num
```

## Explanation
* The solution is based on [Rejection Sampling](https://en.wikipedia.org/wiki/Rejection_sampling), which basically means that if the number generated is not within the desired range, then resample the number

## Code Dissection
1. The given function is a simple random number generator that produces 0 or 1 with equal probability
    ```python
    def zero_one_random():
        return random.randrange(2)
    ```
2. Set a variable _p_ that represents our desired probability range, using the given lower_bound and upper_bound
    ```python
    p = upper_bound - lower_bound + 1
    ```
    * The reason + 1 is added to p, is because the stopping of a random range is excluded from the range
    * For instance, if you wanted to generate a random number for a dice roll [1, 6], the number 6 should be included in the range
3. Loop until a uniform random number is generated
    ```python
    while True:
    ```
4. Initialize the random number and a resample loop iterator to zero
    ```python
    num = 0
    i = 0
    ```
5. Create a loop that runs until _i_ &times; 2 is outside the desired range _p_
    ```python
    while 1 << i < p:
    ```
6. Generate a random number using the given random number generator and increment _i_
    ```python
    num = num << 1 | zero_one_random()
    i += 1
    ```
7. If the random number is within the desired range _p_, stop the resample loop, because the uniform random number has been found
    ```python
    if num < p:
        break
    ```
8. Return the uniform random number
    ```python
    return num
    ```

## Useful References
* [Python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)