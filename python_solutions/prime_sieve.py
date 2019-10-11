from test_framework import generic_test


def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for i in range(i * i, n + 1, i):
                sieve[i] = False
    return primes


if __name__ == '__main__':
    exit(generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv", generate_primes))
