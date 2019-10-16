# Enumerate All Primes to _n_
A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.

Write a program that takes an integer argument and returns all the primes between 1 and that integer.

## Example
```
 Input: 20
Output: [2, 3, 5, 7, 11, 13, 17, 19]
```

## Solution
```python
def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for i in range(i * i, n + 1, i):
                sieve[i] = False
    return primes
```

## Explanation
* The brute-force algorithm is to use [Trial Division](https://en.wikipedia.org/wiki/Trial_division)
* The solution uses the algorithm [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
* The basic idea of the Sieve of Eratosthenes is to use a table of numbers 1 to _n_; for every prime number we find, we eliminate the multiples of that number since they must be composite

## Code Dissection
1. Create an array to hold the prime numbers and a boolean array initialized to True for numbers 1 to _n_
    ```python
    primes = []
    sieve = [True] * (n + 1)
    ```
2. Loop over the numbers from 2 to _n_, we start at 2, since 1 is composite
    ```python
    for i in range(2, n + 1):
    ```
3. If the bool in the sieve[_i_] is True, then _i_ is prime and added to primes[]
    ```python
    if sieve[i]:
        primes.append(i)
    ```
4. If _i_ is prime, then all multiples of _i_ are composite (such as 2 &times; 2 = 4, and 4 is not prime)
    ```python
    for i in range(i * i, n + 1, i):
        sieve[i] = False
    ```
    * `i * i` finds the multiples of _i_
    * `n +  1` simply defines the limit of the loop
    * `i` defines the steps to take in the loop, which is the multiples of _i_
5. Return the list of prime numbers
    ```python
    return primes
    ```

## Useful References
* [Khan Academy - Trial Division](https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/trial-division)
* [Smartick - Sieve of Eratosthenes](https://www.smartickmethod.com/blog/math/operations-and-algebraic-thinking/divisibility/prime-numbers-sieve-eratosthenes/)