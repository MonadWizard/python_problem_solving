# Armstrong Number — Concepts & Approaches

# আর্মস্ট্রং সংখ্যা (Armstrong Number)

একটি **\(n\)**-অংকের পূর্ণসংখ্যা \(N\)–কে তার প্রতিটি অংককে \(n\) ঘাত করে যোগ করলে যদি আবার \(N\)–ই ফিরে আসে, তাহলে সেটি আর্মস্ট্রং সংখ্যা।

## গাণিতিক সংজ্ঞা

যদি \(N = d_1 d_2 \ldots d_n\) (অংকগুলো) হয়, তবে  
\[
N = d_1^{\,n} + d_2^{\,n} + \cdots + d_n^{\,n}
\]

## উদাহরণ

- **153** (৩ অংক):  
  \[
  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
  \]  
  ⇒ আর্মস্ট্রং

- **370, 371, 407** — এরা সব ৩-অংকের আর্মস্ট্রং।

- **9474** (৪ অংক):  
  \[
  9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
  \]  
  ⇒ আর্মস্ট্রং

- **0** ও **1** — দুটিই আর্মস্ট্রং ধরা হয়।

- **10** (২ অংক):  
  \[
  1^2 + 0^2 = 1 \neq 10
  \]  
  ⇒ আর্মস্ট্রং নয়

## কীভাবে যাচাই করবেন

1. সংখ্যার অংকের সংখ্যা \(n\) বের করুন।  
2. প্রতিটি অংককে \(n\) ঘাত করে যোগ করুন।  
3. যোগফলটি মূল সংখ্যার সমান হলে আর্মস্ট্রং; নইলে নয়।

## নোট

- এই সংজ্ঞা সাধারণত **দশমিক (base-10)** পদ্ধতির জন্য প্রযোজ্য।  
- অন্য বেসে সংজ্ঞা দিলে যাচাই পদ্ধতিও সেই বেস অনুযায়ী হবে।



**Problem:** Given an integer `N`, return `True` if it is an **Armstrong (Narcissistic)** number, else `False`.

> A number is Armstrong if it equals the sum of its digits each raised to the power of the number of digits.  
> Example: `153 = 1^3 + 5^3 + 3^3`, `371 = 3^3 + 7^3 + 1^3`.

---

## Edge Cases & Notes
- Zero: `0` has one digit and `0^1 = 0` → **True**.
- Negative integers are **not** Armstrong numbers (by common definition).
- Let `d` be the number of digits in `|N|` (i.e., `d = len(str(abs(N)))`).

---

## Approach 1 — Brute Force (String-based)
**Idea:** Convert to string, count digits `d`, then sum `int(ch) ** d` for each character.

**Algorithm**
1. If `N < 0` → `False`. If `N == 0` → `True`.
2. `s = str(N)` (or `str(abs(N))`), `d = len(s)`.
3. Compute `total = sum(int(ch) ** d for ch in s)`.
4. Return `total == N`.

**Time Complexity:** `O(d)` (iterate digits once).  
**Space Complexity:** `O(d)` due to the string; arithmetic is constant extra.

**Pros/Cons:** Easiest to implement, but uses string conversion.

---

## Approach 2 — Better (Numeric digit extraction)
**Idea:** Avoid strings. Extract digits with `% 10` and `// 10`. Precompute powers for digits `0..9` with exponent `d` to avoid repeated exponentiation.

**Algorithm**
1. If `N < 0` → `False`. If `N == 0` → `True`.
2. `x = abs(N)`, `d = floor(log10(x)) + 1` (or compute via a loop), but simplest is `d = len(str(x))` even if we avoid strings later.
3. Precompute `p = [i**d for i in range(10)]`.
4. Loop while `x > 0`: `digit = x % 10`; accumulate `p[digit]`; `x //= 10`.
5. Compare sum with `abs(N)` (or `N` since `N >= 0`).

**Time Complexity:** `O(d)`; precompute is `O(10)` constant.  
**Space Complexity:** `O(1)` extra (fixed-size table of 10).

**Pros/Cons:** No per-digit string overhead; efficient and clear mathematically.

---

## Approach 3 — Optimal (Numeric + Early Exit pruning)
**Idea:** Same as Approach 2 but **short-circuit** when the running sum already exceeds `N`. This can save work for many non-Armstrong inputs.

**Algorithm**
1. Handle negatives and zero as before.
2. Precompute power table for `d` as above.
3. While extracting digits, keep `running += p[digit]` and if `running > N`, return `False` early.
4. At the end, return `running == N`.

**Time Complexity:** Worst-case `O(d)`, but often faster due to early termination.  
**Space Complexity:** `O(1)` extra.

---

## Comparison

| Approach | Idea | Time | Space | Notes |
|---|---|---|---|---|
| Brute Force | Use string, sum digit^d | O(d) | O(d) | Simplest, uses string |
| Better | Numeric with precomputed digit^d | O(d) | O(1) | No strings, efficient |
| Optimal | Numeric + early exit | ≤ O(d) | O(1) | Often prunes early |

---

## Examples
- `N = 153` → `True` (3 digits: `1^3 + 5^3 + 3^3 = 153`)
- `N = 371` → `True` (3 digits: `3^3 + 7^3 + 1^3 = 371`)
- `N = 10` → `False` (2 digits: `1^2 + 0^2 = 1`)
