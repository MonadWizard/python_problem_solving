# GCD of Two Numbers — Concepts & Approaches

**Problem:** Given two integers `N1` and `N2`, find their Greatest Common Divisor (GCD) — the largest integer that divides both.

**Examples**
- `N1=9, N2=12` → `3`
- `N1=20, N2=15` → `5`

---

## Edge Cases & Conventions
- `gcd(a, 0) = |a|` and `gcd(0, b) = |b|`.
- `gcd(0, 0)` is mathematically undefined; in programming, it’s often returned as `0`.
- For negative inputs, GCD is defined on absolute values: `gcd(a, b) = gcd(|a|, |b|)`.

---

## Approach 1 — Brute Force (Check all divisors up to min)
**Idea:** Try every integer `d` from `1` to `m = min(|a|, |b|)` and keep the largest that divides both.

**Algorithm**
1. Let `a = abs(N1)`, `b = abs(N2)`, `m = min(a, b)`.
2. Initialize `ans = 0`.
3. For `d` in `1..m`:
   - If `a % d == 0` and `b % d == 0`, set `ans = d`.
4. Return `ans`.

**Time Complexity:** `O(m)` where `m = min(|N1|, |N2|)`.  
**Space Complexity:** `O(1)`.

---

## Approach 2 — Better (Enumerate divisors up to √min with pairing)
**Idea:** Any divisor greater than `√m` has a paired divisor less than or equal to `√m`. Enumerate `i` from `1` to `⌊√m⌋`.  
If `i` divides both, update candidate; also check paired divisor `m // i` if it divides both. This reduces checks from `m` to ~`√m`.

**Algorithm**
1. Let `a = abs(N1)`, `b = abs(N2)`, `m = min(a, b)`.
2. Initialize `ans = 0`.
3. For `i` in `1..⌊√m⌋`:
   - If `a % i == 0` and `b % i == 0`, set `ans = max(ans, i)`.
   - Let `p = m // i`. If `a % p == 0` and `b % p == 0`, set `ans = max(ans, p)`.
4. Return `ans`.

**Time Complexity:** `O(√m)` checks.  
**Space Complexity:** `O(1)`.

---

## Approach 3 — Optimal (Euclidean Algorithm)
**Idea:** Use the identity `gcd(a, b) = gcd(b, a mod b)` and repeat until the remainder is `0`.  
This runs in logarithmic time relative to the input size.

**Algorithm**
1. Let `a = abs(N1)`, `b = abs(N2)`.
2. While `b != 0`: `(a, b) = (b, a % b)`.
3. Return `a`.

**Time Complexity:** `O(log(min(|N1|, |N2|)))` — specifically bounded by the number of digits; very fast in practice.  
**Space Complexity:** `O(1)`.

---

## Comparison

| Approach | Idea | Time | Space | Notes |
|---|---|---|---|---|
| Brute Force | Try all divisors up to `min` | O(min) | O(1) | Simple but slow for large inputs |
| Better | Check up to `√min` with paired divisors | O(√min) | O(1) | Good improvement using number theory |
| Optimal | Euclidean algorithm | O(log min) | O(1) | Standard, fastest and cleanest |

---

## Why Euclid is Preferred
It’s the industry-standard solution: tiny code, very fast, and numerically robust. √-based divisor enumeration is helpful conceptually and sometimes useful when you need all common divisors, but for just the GCD Euclid wins.
