# Check if a Number is Prime — Concepts & Approaches

**Problem:** Given an integer `N`, determine whether it is **prime**.  
A prime number has exactly two positive divisors: `1` and itself.

**Examples**
- `N = 2` → `True`
- `N = 10` → `False` (divisible by 2 and 5, among others)

---

## Edge Cases & Notes
- `N <= 1` → **not prime** by definition.
- `N = 2 or 3` → **prime** (smallest primes).
- Negative numbers are not prime.
- We only consider **positive divisors**.

---

## Approach 1 — Brute Force (Try All Divisors 2..N-1)
**Idea:** Check divisibility of every integer from `2` to `N-1`. If any divides `N`, it’s not prime.

**Algorithm**
1. If `N <= 1` → `False`; if `N <= 3` → `True`.
2. For each `d` in `2..N-1`: if `N % d == 0` → `False`.
3. Otherwise `True`.

**Time Complexity:** `O(N)` checks.  
**Space Complexity:** `O(1)`.

**Pros/Cons:** Trivial to implement but far too slow for large `N`.

---

## Approach 2 — Better (Check up to √N)
**Idea:** If `N` has a non-trivial divisor, at least one is `≤ √N`. So we only test `2..⌊√N⌋`.

**Algorithm**
1. If `N <= 1` → `False`; if `N <= 3` → `True`.
2. For `d` in `2..⌊√N⌋`: if `N % d == 0` → `False`.
3. Otherwise `True`.

**Time Complexity:** `O(√N)` checks.  
**Space Complexity:** `O(1)`.

**Pros/Cons:** Big improvement; standard approach for single primality checks.

---

## Approach 3 — Optimal (Skip Multiples using 6k ± 1)
**Idea:** Beyond `2` and `3`, primes are of the form `6k ± 1`. After ruling out small cases and divisibility by `2` and `3`, check only `i = 5, 11, 17, ...` and `i + 2` pairs up to `√N`.

**Algorithm**
1. Handle `N <= 3` quickly, and reject if divisible by `2` or `3`.
2. Set `i = 5`. While `i * i <= N`:
   - If `N % i == 0` or `N % (i + 2) == 0` → `False`.
   - `i += 6`.
3. Return `True`.

**Time Complexity:** `O(√N/3)` (constant-factor speedup vs plain √N).  
**Space Complexity:** `O(1)`.

**Pros/Cons:** Simple, fast, interview-friendly. For extremely large `N` or many queries, advanced methods (segmented sieve, deterministic Miller–Rabin for 32/64-bit) may be preferred.

---

## Comparison

| Approach | Idea | Time | Space | Notes |
|---|---|---|---|---|
| Brute Force | Try all d in 2..N-1 | O(N) | O(1) | Very slow |
| Better | Try up to √N | O(√N) | O(1) | Standard |
| Optimal | 6k ± 1 skipping | ~O(√N/3) | O(1) | Fewer checks than plain √N |

---

## Practical Tips
- Always handle small cases first (`N <= 3`).
- Early rejections for even (`N % 2 == 0`) and divisible by 3 numbers.
- For batch checking up to large limits (e.g., 10^7), use a sieve of Eratosthenes.
