# LeetCode 9: Palindrome Number
# Implementations of three approaches with quick tests.

def is_palindrome_half(x: int) -> bool:
    """
    Approach A (Optimal): Reverse half of the number.
    Time: O(d), Space: O(1)
    """
    if x < 0:
        return False
    if x % 10 == 0 and x != 0:
        return False

    rev = 0
    while x > rev:
        rev = rev * 10 + (x % 10)
        x //= 10

    # Even digits: x == rev
    # Odd digits: ignore middle digit of rev (rev // 10)
    return x == rev or x == rev // 10


def is_palindrome_full_reverse(x: int) -> bool:
    """
    Approach B: Reverse the whole number numerically and compare.
    Time: O(d), Space: O(1)
    """
    if x < 0:
        return False
    # Optional early break (not required for correctness):
    if x % 10 == 0 and x != 0:
        return False

    orig = x
    rev = 0
    while x:
        rev = rev * 10 + (x % 10)
        x //= 10
    return rev == orig


def is_palindrome_string(x: int) -> bool:
    """
    Approach C: String two-pointer (or s == s[::-1]).
    Time: O(d), Space: O(d)
    """
    if x < 0:
        return False
    s = str(x)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# ------------------
# Quick self-test
# ------------------
if __name__ == "__main__":
    tests = [0, 5, 9, 10, 11, 121, 1221, 12321, -121, 1001, 100, 1000000001]
    for t in tests:
        a = is_palindrome_half(t)
        b = is_palindrome_full_reverse(t)
        c = is_palindrome_string(t)
        print(f"x={t:>12} | A={str(a):>5} | B={str(b):>5} | C={str(c):>5}")