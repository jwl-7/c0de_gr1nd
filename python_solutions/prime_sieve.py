from test_framework import generic_test


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    exit(generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv", generate_primes))