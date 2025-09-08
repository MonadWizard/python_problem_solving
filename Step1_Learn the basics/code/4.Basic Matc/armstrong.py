# armstrong.py — Three approaches to check Armstrong Number
# Approaches: Brute Force (string), Better (numeric), Optimal (numeric + early exit)
# Includes a quick self-test.

from typing import List

def is_armstrong_bruteforce(n: int) -> bool:
    """
    Approach 1: String-based.
    Time: O(d), Space: O(d)
    """
    if n < 0:
        return False
    if n == 0:
        return True
    s = str(n)
    d = len(s)
    total = sum(int(ch) ** d for ch in s)
    return total == n


def is_armstrong_better(n: int) -> bool:
    """
    Approach 2: Numeric digit extraction with precomputed powers.
    Time: O(d), Space: O(1)
    """
    if n < 0:
        return False
    if n == 0:
        return True
    x = n
    d = len(str(x))  # could compute via loop/log as well
    pows: List[int] = [i ** d for i in range(10)]
    total = 0
    while x > 0:
        digit = x % 10
        total += pows[digit]
        x //= 10
    return total == n


def is_armstrong_optimal(n: int) -> bool:
    """
    Approach 3: Numeric + early exit pruning.
    Time: O(d) worst-case (often less), Space: O(1)
    """
    if n < 0:
        return False
    if n == 0:
        return True
    x = n
    d = len(str(x))
    pows: List[int] = [i ** d for i in range(10)]
    total = 0
    while x > 0:
        digit = x % 10
        total += pows[digit]
        if total > n:  # early exit
            return False
        x //= 10
    return total == n


# ------------------
# Quick self-test
# ------------------
if __name__ == "__main__":
    tests = [
        (0, True),
        (1, True),
        (2, True),
        (5, True),
        (9, True),
        (10, False),
        (153, True),
        (370, True),
        (371, True),
        (407, True),
        (9474, True),      # 4-digit Armstrong
        (9475, False),
        (9926315, True),   # 7-digit Armstrong
    ]
    for t, want in tests:
        a = is_armstrong_bruteforce(t)
        b = is_armstrong_better(t)
        c = is_armstrong_optimal(t)
        ok = (a == want) and (b == want) and (c == want)
        print(f"n={t:>9} | brute={a!s:>5} | better={b!s:>5} | optimal={c!s:>5} | ok={ok}")
