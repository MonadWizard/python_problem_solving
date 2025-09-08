# Reverse Integer — Concepts & Complexity

**Problem (LeetCode 7):** Given a signed 32-bit integer `x`, return the digits of `x` reversed.  
If the reversed integer overflows outside **[-2^31, 2^31 - 1]**, return **0**.

- Example: `x = 123` → `321`
- Example: `x = -120` → `-21`
- Example: `x = 1534236469` → reverse would overflow → `0`

Let:
- `INT_MIN = -2^31 = -2147483648`
- `INT_MAX =  2^31 - 1 =  2147483647`

---

## Approach A — Optimal: Pop/Push Digits (Math, O(1) extra space)

**Idea:** Iteratively pop the last digit of `x` (`pop = x % 10` / `x //= 10`, adjusted for negative), and push it into the result `rev = rev*10 + pop`.  
Before pushing, **check for overflow** using thresholds derived from `INT_MAX` and `INT_MIN`:

- If `rev > INT_MAX // 10` → overflow on next push
- If `rev == INT_MAX // 10 and pop > 7` → overflow (since `INT_MAX` ends with 7)
- If `rev < INT_MIN // 10` → underflow on next push
- If `rev == INT_MIN // 10 and pop < -8` → underflow (since `INT_MIN` ends with -8)

**Why this works:** It mirrors what you’d write in C++/Java, independent of Python’s big-int behavior.

**Time Complexity:** `O(d)`, where `d` = number of digits (each digit handled once).  
**Space Complexity:** `O(1)`.

---

## Approach B — String Reverse with Bounds Check (Simple, O(d) extra space)

**Idea:** Convert to string, manage sign, reverse the character array, convert back to int, then return `0` if out of range.

**Steps:**
1. Remember if `x < 0` (sign).
2. Reverse the absolute string: `s[::-1]`.
3. Parse back to int and re-apply sign.
4. If outside `[INT_MIN, INT_MAX]`, return `0`.

**Time Complexity:** `O(d)` for building the reversed string.  
**Space Complexity:** `O(d)` due to string/array.

---

## Approach C — Pythonic Slice + Math Bound Check (Concise)

**Idea:** Use slicing for reversal, but still handle sign and the 32-bit bounds exactly.  
This is essentially a more compact variant of Approach B, but kept explicit about the range check.

**Time Complexity:** `O(d)` (string ops).  
**Space Complexity:** `O(d)`.

---

## Notes on Edge Cases

- `x = 0` → `0`
- Trailing zeros vanish after reverse (e.g., `-120` → `-21`).
- Single-digit numbers return themselves.
- Always **check 32-bit bounds** *after* forming the reversed number (or via pre-check thresholds in Approach A).

---

## Why Approach A is often preferred

In languages with fixed-width integers (C++/Java), Approach A avoids building strings and demonstrates safe overflow handling using arithmetic thresholds. It’s memory-constant and interview-friendly.