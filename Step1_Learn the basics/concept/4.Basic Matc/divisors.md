# Print All Divisors of a Given Number — Concepts & Approaches

**Problem:** Given an integer `N` (assume `N > 0`), return all **positive** divisors of `N`.

**Examples**
- `N = 36` → `[1, 2, 3, 4, 6, 9, 12, 18, 36]`
- `N = 12` → `[1, 2, 3, 4, 6, 12]`

---

## Edge Cases & Conventions
- If `N == 1`, divisors = `[1]`.
- If `N` is prime, divisors = `[1, N]`.
- This problem usually considers **positive** divisors only.

Let `τ(N)` denote the number of divisors of `N` (output size). Any algorithm must spend at least `Ω(τ(N))` time to output them.

---

## Approach 1 — Brute Force (Check all from 1..N)
**Idea:** Test every `d` from `1` to `N`. If `N % d == 0`, append `d`.

**Algorithm**
1. Initialize `ans = []`.
2. For `d` in `1..N`:
   - If `N % d == 0`, append `d`.
3. Return `ans`.

**Time Complexity:** `O(N)` divisibility checks.  
**Space Complexity:** `O(τ(N))` for the output list.

**Pros/Cons:** Trivial to implement but slow for large `N`.

---

## Approach 2 — Better (Check up to N/2, plus N)
**Idea:** Any non-trivial divisor (other than `N`) is at most `N/2`. So check `1..⌊N/2⌋`, collect divisors, and finally append `N`.

**Algorithm**
1. Initialize `ans = [1]` (if `N > 1`).
2. For `d` in `2..⌊N/2⌋`:
   - If `N % d == 0`, append `d`.
3. Append `N`.
4. Return `ans`.

**Time Complexity:** `O(N)` in the worst case (slightly better constants than Approach 1).  
**Space Complexity:** `O(τ(N))`.

**Pros/Cons:** Still linear in `N` but avoids one extra check. Generally not a significant upgrade; mainly useful as a stepping stone.

---

## Approach 3 — Optimal (Enumerate up to √N and pair divisors)
**Idea:** If `d` divides `N`, then `N/d` also divides `N`. One of the pair is `≤ √N` and the other is `≥ √N`.  
Enumerate `d` from `1` to `⌊√N⌋`. For each divisor found, add **both** `d` and `N//d`. To return in sorted order without a separate sort, store small divisors and large divisors separately and concatenate.

**Algorithm**
1. Initialize `small = []`, `large = []`.
2. For `d` in `1..⌊√N⌋`:
   - If `N % d == 0`:
     - Append `d` to `small`.
     - If `d != N//d`, append `N//d` to `large`.
3. Result = `small + reversed(large)` (sorted ascending).
4. Return result.

**Time Complexity:** `O(√N)` divisibility checks, plus `O(τ(N))` to build the output.  
**Space Complexity:** `O(τ(N))` for output; extra `O(√N)` at most for the two helper lists (bounded by number of pairs).

**Pros/Cons:** Standard optimal approach for listing divisors; fast and neat, yields sorted order without an explicit sort.

---

## Comparison

| Approach | Idea | Time | Space | Sorted Output |
|---|---|---|---|---|
| Brute Force | Try all `d` in `1..N` | O(N) | O(τ(N)) | Yes (natural order) |
| Better | Try up to `N/2` then add `N` | O(N) | O(τ(N)) | Yes |
| Optimal | Pair divisors using √N | O(√N) | O(τ(N)) | Yes (small + reversed large) |

---

## Practical Tips
- Use the √N method for large inputs.
- Use `math.isqrt(N)` for integer square root to avoid floating-point inaccuracies.
- If you only need the **count** of divisors, prime factorization is another route; but for listing all divisors, the √N pairing is most direct.
