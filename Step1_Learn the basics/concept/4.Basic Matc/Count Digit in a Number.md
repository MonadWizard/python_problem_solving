# Count Digits in a Number — Concept & Approaches

## Problem
Given an integer `N`, return the number of digits in `N`.

**Examples**
- `N = 12345` → `5`
- `N = 7789` → `4`

## Clarifications & Edge Cases
- **Zero:** `N = 0` has **1** digit.
- **Negative numbers:** Count digits on the absolute value (e.g., `N = -456` → `3`).
- **Large integers:** Python integers are arbitrary-precision; approaches should scale with the number of digits `d`.

---

## Approach 1 — Brute Force (Division-by-10 loop)
**Idea:** Continuously divide `|N|` by `10` and count how many times until it becomes `0`.

**Steps**
1. If `N == 0`, return `1`.
2. Let `x = abs(N)`, `count = 0`.
3. While `x > 0`: do `x //= 10` and increment `count`.
4. Return `count`.

**Time Complexity:** `O(d)` where `d` is the number of digits (≈ `⌊log10(|N|)⌋ + 1`).  
**Space Complexity:** `O(1)`.

**Why it’s “Brute Force”?** It inspects each digit position one by one via repeated division—simple, reliable, but linear in the number of digits.

---

## Approach 2 — Optimal (Logarithm)
**Idea:** Use base-10 logarithm to compute the digit count directly:
- For `N > 0`, digits = `⌊log10(N)⌋ + 1`.
- For `N = 0`, digits = `1`.
- For `N < 0`, apply it to `|N|`.

**Steps**
1. If `N == 0`, return `1`.
2. Let `x = abs(N)`.
3. Return `floor(log10(x)) + 1`.

**Time Complexity:** `O(1)` arithmetic operations (though with floating-point log).  
**Space Complexity:** `O(1)`.

**Caveats**
- Must handle `N = 0` specially (log10(0) is undefined).
- For extremely large integers, floating-point precision can be a concern, but Python’s `math.log10` is typically robust for practical ranges. If absolute robustness is required for **very** large integers, prefer the division loop or `len(str(abs(N)))` (string conversion is also `O(d)`).

---

## Comparison

| Approach | Idea | Time | Space | Notes |
|---|---|---|---|---|
| Brute Force | Repeatedly divide by 10 | O(d) | O(1) | Works for all ints, precise |
| Optimal | Use `log10` | O(1) | O(1) | Needs special-case 0 and care with extreme sizes |