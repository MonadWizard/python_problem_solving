# Palindrome Number — Concepts & Complexity (LeetCode 9)

**Problem:** Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.  
A palindrome reads the same forwards and backwards.

**Examples**

-   `x = 121` → `True`
-   `x = -121` → `False` (minus sign)
-   `x = 10` → `False` (leading zero after reverse)

---

## Approach A — Optimal: Reverse **Half** of the Number (O(1) extra space)

**Key ideas**

-   Negative numbers cannot be palindromes.
-   If `x` ends with `0` but `x != 0`, it cannot be a palindrome (because leading zeros are not allowed).
-   We don’t need to reverse the whole number. Reverse digits until the reversed half is **≥** the remaining half.
-   For even digit counts: `x == reversedHalf`  
    For odd digit counts: `x == reversedHalf // 10` (middle digit ignored).

**Algorithm**

1. If `x < 0` → `False`.
2. If `x % 10 == 0` and `x != 0` → `False`.
3. Let `rev = 0`. While `x > rev`:
    - `rev = rev * 10 + (x % 10)`
    - `x //= 10`
4. Return `x == rev or x == rev // 10`.

**Time Complexity:** `O(d)` where `d` is number of digits (we process ~half).  
**Space Complexity:** `O(1)`.

---

## Approach B — Full Reverse (Numeric), then Compare

**Key ideas**

-   Create a reversed copy of the absolute number using arithmetic (no strings).
-   Compare reversed value with original.
-   Early rejections:
    -   Negative numbers → `False`
    -   Ends-with-zero and not zero → `False` (optional optimization)

**Algorithm**

1. If `x < 0` → `False`.
2. Optionally, if `x % 10 == 0` and `x != 0` → `False`.
3. Reverse `x` fully using `% 10` and `// 10` loop into `y`.
4. Return `y == original_x`.

**Time Complexity:** `O(d)` (each digit processed once).  
**Space Complexity:** `O(1)`.

---

## Approach C — String / Two-Pointer

**Key ideas**

-   Convert `x` to string; negatives fail immediately.
-   Compare characters from both ends toward the center.
-   Equivalent to `s == s[::-1]`, but two-pointer is explicit and avoids building a second full reversed string (although the string itself already costs `O(d)`).

**Algorithm**

1. If `x < 0` → `False`.
2. `s = str(x)`.
3. Initialize `i = 0`, `j = len(s) - 1`; while `i < j`:
    - If `s[i] != `s[j]`→`False`
    - `i += 1`, `j -= 1`
4. Return `True`.

**Time Complexity:** `O(d)` (single pass).  
**Space Complexity:** `O(d)` for the string (in Python, integers must be converted to string).

---

## Edge Cases

-   `x = 0` → `True`
-   Single-digit numbers → `True`
-   Trailing zeros: e.g., `10` → `False`
-   Very large numbers → All numeric approaches remain `O(d)`

---

## Why Approach A is preferred

It achieves `O(1)` extra space and minimal operations by only reversing half the digits and doing precise comparisons, which is ideal for interviews and languages without big integers.
