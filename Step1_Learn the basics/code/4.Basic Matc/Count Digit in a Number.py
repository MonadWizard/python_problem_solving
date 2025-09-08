# Count Digits in a Number — Solutions (Python)

## Brute Force Solution (Division Loop)

def count_digits_bruteforce(n: int) -> int:
    """
    Count digits by repeatedly dividing by 10.
    Handles negatives and zero.
    Time: O(d), Space: O(1)
    """
    if n == 0:
        return 1
    x = abs(n)
    cnt = 0
    while x > 0:
        x //= 10
        cnt += 1
    return cnt

## Optimal Solution (Logarithm)

import math

def count_digits_optimal(n: int) -> int:
    """
    Count digits using floor(log10(|n|)) + 1.
    Special-case zero. Handles negatives.

    Time: O(1) arithmetic, Space: O(1)
    Note: For astronomically large integers, floating precision
    can lead to off-by-one in rare edge cases; fall back to the loop if needed.
    """
    if n == 0:
        return 1
    x = abs(n)
    return int(math.floor(math.log10(x))) + 1

## Quick Tests

if __name__ == "__main__":
    tests = [0, 5, 9, 10, 99, 100, 12345, -456, 7789, -10**12, 10**18 - 1, 10**18]
    for t in tests:
        bf = count_digits_bruteforce(t)
        opt = count_digits_optimal(t)
        print(f"N={t:>22} | brute={bf} | optimal={opt}")
