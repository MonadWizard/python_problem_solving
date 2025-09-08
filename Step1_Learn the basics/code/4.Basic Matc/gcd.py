# gcd.py — Three approaches to compute GCD of two integers
# Approaches: Brute Force, Sqrt-based Better, Euclidean Optimal
# Includes a quick self-test.
from math import isqrt

def gcd_bruteforce(a: int, b: int) -> int:
    """
    Approach 1: Check all divisors up to min(|a|, |b|).
    Time: O(min(|a|, |b|)), Space: O(1)
    """
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0  # convention for programming; mathematically undefined
    if a == 0 or b == 0:
        return a or b
    m = min(a, b)
    ans = 0
    for d in range(1, m + 1):
        if a % d == 0 and b % d == 0:
            ans = d
    return ans


def gcd_sqrt_better(a: int, b: int) -> int:
    """
    Approach 2: Enumerate divisors up to sqrt(min) and use paired divisors.
    Time: O(sqrt(min(|a|, |b|))), Space: O(1)
    """
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0
    if a == 0 or b == 0:
        return a or b
    m = min(a, b)
    ans = 0
    for i in range(1, isqrt(m) + 1):
        if a % i == 0 and b % i == 0:
            if i > ans:
                ans = i
        # check paired divisor
        p = m // i
        if a % p == 0 and b % p == 0:
            if p > ans:
                ans = p
    return ans


def gcd_euclid(a: int, b: int) -> int:
    """
    Approach 3: Euclidean Algorithm
    Time: O(log(min(|a|, |b|))), Space: O(1)
    """
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a


# ------------------
# Quick self-test
# ------------------
if __name__ == "__main__":
    tests = [
        (9, 12, 3),
        (20, 15, 5),
        (0, 0, 0),
        (0, 7, 7),
        (18, 24, 6),
        (101, 103, 1),
        (-48, 18, 6),
        (270, 192, 6),
        (10**6, 10**4, 10**4),
    ]
    for x, y, want in tests:
        b1 = gcd_bruteforce(x, y)
        b2 = gcd_sqrt_better(x, y)
        b3 = gcd_euclid(x, y)
        ok = (b1 == want) and (b2 == want) and (b3 == want)
        print(f"gcd({x},{y}) -> brute={b1}, sqrt={b2}, euclid={b3}  | ok={ok}")
