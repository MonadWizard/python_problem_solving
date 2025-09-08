# 3 solutions for LeetCode 7: Reverse Integer
# Range must be 32-bit signed: [-2**31, 2**31 - 1]

INT_MIN = -2**31       # -2147483648
INT_MAX =  2**31 - 1   #  2147483647


def reverse_integer_math(x: int) -> int:
    """
    Approach A (Optimal): Pop/Push digits with overflow checks.
    Time: O(d), Space: O(1)
    """
    rev = 0
    while x != 0:
        # Python's % and // with negatives behave differently than C.
        # To pop the last digit in a sign-agnostic way:
        pop = int(x % 10) if x >= 0 else int(x % -10)  # works but clearer to use math below
        # A clearer cross-language-like pop is:
        pop = x % 10 if x >= 0 else x % -10
        # But to be precise and simple, use:
        pop = x - (x // 10) * 10  # last digit preserving sign
        x //= 10

        # Overflow checks prior to pushing
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0
        if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and pop < -8):
            return 0

        rev = rev * 10 + pop
    return rev


def reverse_integer_string(x: int) -> int:
    """
    Approach B: String reverse with explicit bounds check.
    Time: O(d), Space: O(d)
    """
    sign = -1 if x < 0 else 1
    s = str(abs(x))[::-1]
    val = sign * int(s) if s else 0
    return val if INT_MIN <= val <= INT_MAX else 0


def reverse_integer_pythonic(x: int) -> int:
    """
    Approach C: Compact Pythonic slicing + bounds check.
    Time: O(d), Space: O(d)
    """
    if x < 0:
        val = -int(str(-x)[::-1])
    else:
        val = int(str(x)[::-1])
    return val if INT_MIN <= val <= INT_MAX else 0


# ------------------
# Quick self-test
# ------------------
if __name__ == "__main__":
    tests = [0, 5, 10, -120, 123, -123, 1534236469, 1463847412, 2147483647, -2147483412]
    for t in tests:
        a = reverse_integer_math(t)
        b = reverse_integer_string(t)
        c = reverse_integer_pythonic(t)
        print(f"x={t:>12} | A={a:>12} | B={b:>12} | C={c:>12}")