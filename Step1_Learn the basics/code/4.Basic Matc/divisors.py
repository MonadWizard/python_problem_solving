# divisors.py — Three approaches to list all positive divisors of N
# Approaches: Brute Force, Better (to N/2), Optimal (sqrt pairing)
# Includes a quick self-test.

from math import isqrt
from typing import List

def divisors_bruteforce(n: int) -> List[int]:
    """
    Approach 1: Check all d in [1..n].
    Time: O(n), Space: O(τ(n)) for output.
    Requires n >= 1.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    ans = []
    for d in range(1, n + 1):
        if n % d == 0:
            ans.append(d)
    return ans


def divisors_better_half(n: int) -> List[int]:
    """
    Approach 2: Check up to n//2 and append n at the end.
    Time: O(n), Space: O(τ(n)) for output.
    Requires n >= 1.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return [1]
    ans = [1]
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            ans.append(d)
    ans.append(n)
    return ans


def divisors_optimal_sqrt(n: int) -> List[int]:
    """
    Approach 3: Enumerate up to sqrt(n); collect pairs to get sorted output.
    Time: O(sqrt(n)), Space: O(τ(n)) for output.
    Requires n >= 1.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    small, large = [], []
    r = isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            small.append(d)
            other = n // d
            if other != d:
                large.append(other)
    # small is increasing; large holds larger divisors in increasing discovery order
    # reverse large to make the final list sorted
    return small + large[::-1]


# ------------------
# Quick self-test
# ------------------
if __name__ == "__main__":
    tests = [1, 2, 3, 4, 6, 12, 36, 97, 100, 10**6]
    for t in tests:
        b1 = divisors_bruteforce(t)
        b2 = divisors_better_half(t)
        b3 = divisors_optimal_sqrt(t)
        ok = (b1 == b2 == b3)
        print(f"n={t:<10} | brute={len(b1):>4} divs | ok={ok} | sample={b3[:10]}{'...' if len(b3)>10 else ''}")
