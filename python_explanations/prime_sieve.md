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
* The brute-force algorithm is to use [Trial Division](https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/trial-division)  
* The solution uses the algorithm [Sieve of Eratosthenes](https://www.smartickmethod.com/blog/math/operations-and-algebraic-thinking/divisibility/prime-numbers-sieve-eratosthenes/)  
* The basic idea of the Sieve of Eratosthenes is to use a table of numbers 1 to _n_, and for every prime number we fine, we eliminate the multiples of that number since they must be composite  
  
## Code Dissection
1. [FILL IN]