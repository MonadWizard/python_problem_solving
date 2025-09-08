# prime.py — Three approaches to test primality
# Approaches: Brute Force, Sqrt-based, Optimal 6k±1
# Includes a quick self-test.

from math import isqrt

def is_prime_bruteforce(n: int) -> bool:
    """
    Approach 1: Try all divisors from 2..n-1.
    Time: O(n), Space: O(1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def is_prime_sqrt(n: int) -> bool:
    """
    Approach 2: Try divisors up to floor(sqrt(n)).
    Time: O(sqrt(n)), Space: O(1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    r = isqrt(n)
    for d in range(2, r + 1):
        if n % d == 0:
            return False
    return True


def is_prime_6k1(n: int) -> bool:
    """
    Approach 3: 6k ± 1 optimization.
    Time: O(sqrt(n)/3), Space: O(1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return n in (2, 3)  # already handled <=3, but keeps it safe
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ------------------
# Quick self-test
# ------------------
if __name__ == "__main__":
    tests = [0, 1, 2, 3, 4, 5, 10, 11, 25, 29, 97, 221, 9973, 10**9 + 7]
    for t in tests:
        b1 = is_prime_bruteforce(t) if t < 10000 else 'skip'  # skip huge for brute
        b2 = is_prime_sqrt(t)
        b3 = is_prime_6k1(t)
        same = (b2 == b3) and (b1 == 'skip' or b1 == b2)
        print(f"n={t:<12} | brute={b1} | sqrt={b2} | 6k±1={b3} | ok={same}")
