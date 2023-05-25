def get_primes(n: int):
    _primes = [True for _ in range(n + 1)]

    _primes[0] = False
    _primes[1] = False

    for i in range(2, n + 1):
        if _primes[i]:
            for j in range(2 * i, n + 1, i):
                _primes[j] = False

    return _primes
